"""
Core function for extracting polynomial patterns from time series data.
"""

from typing import Optional, Union, List, Dict, Tuple, Any
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from numpy.typing import NDArray
import matplotlib
matplotlib.use('Agg')
import optuna

from .models import LightGBMModel
from sklearn.metrics import accuracy_score, roc_auc_score, mean_squared_error

optuna.logging.set_verbosity(optuna.logging.WARNING)

def evaluate_model_performance(model, X_combined, y_train, val_size, metric):
    X_train, X_val, y_train_split, y_val = train_test_split(X_combined, y_train, test_size=val_size, random_state=42)
    model.fit(X_train, y_train_split, X_val, y_val)
    if metric == 'auc':
        y_pred = model.predict_proba(X_val)
        return roc_auc_score(y_val, y_pred, multi_class='ovr', average='macro') if len(np.unique(y_val)) > 2 else roc_auc_score(y_val, y_pred)
    elif metric == 'accuracy':
        return accuracy_score(y_val, model.predict(X_val))
    elif metric == 'rmse':
        return np.sqrt(mean_squared_error(y_val, model.predict(X_val)))

def feature_extraction(input_series_train: Union[pd.DataFrame, List[pd.DataFrame]], 
                      y_train: Union[pd.Series, np.ndarray], 
                      input_series_test: Optional[Union[pd.DataFrame, List[pd.DataFrame]]] = None,
                      initial_features: Optional[Union[NDArray[np.float32], Tuple[NDArray[np.float32], NDArray[np.float32]]]] = None,
                      model: Optional[Any] = None, 
                      metric: Optional[str] = None, 
                      polynomial_degree: int = 3, 
                      val_size: float = 0.2,
                      n_trials: int = 300, 
                      n_jobs: int = -1, 
                      show_progress: bool = True) -> Dict[str, Any]:
    
    # Convert input time series/spatial data to numpy arrays
    if isinstance(input_series_train, list):
        # Multivariate: list of DataFrames, each representing a different time series or spatial dimension
        input_series_train = np.stack([df.values.astype(np.float32) for df in input_series_train], axis=1)
        if input_series_test is not None:
            input_series_test = np.stack([df.values.astype(np.float32) for df in input_series_test], axis=1)
        else:
            input_series_test = None
    else:
        # Univariate: single DataFrame representing one time series or spatial data
        input_series_train = input_series_train.values.astype(np.float32)
        if input_series_test is not None:
            input_series_test = input_series_test.values.astype(np.float32)
        else:
            input_series_test = None
    
    y_train_array = y_train.values.astype(np.float32) if isinstance(y_train, pd.Series) else np.asarray(y_train, dtype=np.float32)
    
    # Get input series dimensions
    n_input_series = input_series_train.shape[1] if input_series_train.ndim == 3 else 1
    n_time_points = input_series_train.shape[2] if input_series_train.ndim == 3 else input_series_train.shape[1]

    # Initialize the feature set that will be fed to the ML model
    if initial_features:
        if isinstance(initial_features, tuple) and len(initial_features) == 2:
            initial_features_train, initial_features_test = np.asarray(initial_features[0], dtype=np.float32), np.asarray(initial_features[1], dtype=np.float32)
        else:
            initial_features_train, initial_features_test = np.asarray(initial_features, dtype=np.float32), None
        model_features_list = [initial_features_train]
    else:
        initial_features_train, initial_features_test = None, None
        model_features_list = []
    
    # Auto-detect metric if not provided
    if not metric:
        unique_targets = len(np.unique(y_train_array))
        metric = 'auc' if unique_targets == 2 else 'accuracy' if unique_targets > 2 else 'rmse'
    
    # Auto-create model if not provided
    if not model:
        is_classification = metric in ['auc', 'accuracy']
        n_classes = len(np.unique(y_train_array)) if is_classification else None
        model = LightGBMModel('classification' if is_classification else 'regression', n_classes)
    best_score = float('inf') if metric == 'rmse' else -float('inf')
    
    # Generate polynomial pattern values using polynomial function
    def generate_polynomial_pattern(coeffs: List[float], width: int) -> NDArray[np.float32]:
        return np.sum(np.array(coeffs, dtype=np.float32) * (np.linspace(-1, 1, width, dtype=np.float32)[:, None] ** np.arange(len(coeffs), dtype=np.float32)), axis=1)
    
    # Calculate RMSE between input series region and pattern (this becomes a feature for the ML model)
    def calculate_pattern_rmse(X_region: NDArray[np.float32], pattern_values: NDArray[np.float32]) -> NDArray[np.float32]:
        return np.sqrt(np.mean((X_region - pattern_values) ** 2, axis=1))

    def objective(trial: optuna.Trial) -> float:
        # Select which input series to extract pattern from (only for multivariate)
        input_series_idx = trial.suggest_int('series_index', 0, n_input_series - 1) if n_input_series > 1 else 0
        
        # Select pattern location and size in the input series
        pattern_start = trial.suggest_int('pattern_start', 0, n_time_points - 2)
        pattern_width = trial.suggest_int('pattern_width', 1, n_time_points - pattern_start)
        
        # Generate polynomial coefficients for the pattern
        coeffs = [trial.suggest_float(f'c{i}', -1, 1) for i in range(polynomial_degree + 1)]
        
        # Extract the specific input series data
        if n_input_series > 1:
            selected_input_series = input_series_train[:, input_series_idx, :]
        else:
            selected_input_series = input_series_train
        
        # Extract the pattern region from the input series
        pattern_region = selected_input_series[:, pattern_start:pattern_start + pattern_width]
        
        # Generate the polynomial pattern values
        pattern_vals = generate_polynomial_pattern(coeffs, pattern_width)

        # Calculate RMSE between input series region and pattern (this becomes a feature for the ML model)
        new_model_feature = calculate_pattern_rmse(pattern_region, pattern_vals)
        
        # Combine with existing features to create the complete feature set for the ML model
        model_feature_set = np.column_stack(model_features_list + [new_model_feature]) if model_features_list else new_model_feature.reshape(-1, 1)
        return evaluate_model_performance(model, model_feature_set, y_train_array, val_size, metric)
    
    # Extract multiple patterns from input series to build the feature set
    extracted_patterns = []
    pattern_starts = []
    pattern_widths = []
    pattern_series_indices = []
    first_pattern = True
    
    while True:
        study = optuna.create_study(direction="minimize" if metric == 'rmse' else "maximize", pruner=optuna.pruners.MedianPruner())
        study.optimize(objective, n_trials=n_trials, n_jobs=n_jobs, show_progress_bar=show_progress)
        
        if first_pattern or (metric == 'rmse' and study.best_value < best_score) or (metric != 'rmse' and study.best_value > best_score):
            best_score = study.best_value
            best_params = study.best_trial.params
            start, width = best_params['pattern_start'], best_params['pattern_width']
            input_series_idx = best_params.get('series_index', 0)
            coeffs = [best_params[f'c{i}'] for i in range(polynomial_degree + 1)]
            
            # Generate the polynomial pattern using the function
            pattern_vals = generate_polynomial_pattern(coeffs, width)
            extracted_patterns.append(pattern_vals)
            pattern_starts.append(start)
            pattern_widths.append(width)
            pattern_series_indices.append(input_series_idx)
            
            # Extract the corresponding input series data and generate a feature for the ML model
            if n_input_series > 1:
                selected_input_series = input_series_train[:, input_series_idx, :]
            else:
                selected_input_series = input_series_train
            
            # Calculate RMSE feature from this pattern and add to the model feature set
            pattern_feature = calculate_pattern_rmse(selected_input_series[:, start:start+width], pattern_vals)
            model_features_list.append(pattern_feature)
            first_pattern = False
        else:
            break
    
    # Combine all extracted pattern features into the final feature set for the ML model
    model_features = np.column_stack(model_features_list) if model_features_list else np.empty((input_series_train.shape[0], 0))
    
    # Split the feature set for training and validation
    train_features, val_features, y_train, y_val = train_test_split(model_features, y_train, test_size=val_size, random_state=42)
    model.fit(train_features, y_train, val_features, y_val)
    
    # Apply the same pattern extraction to test data to create test features
    test_features = None
    if input_series_test is not None:
        n_test_samples = input_series_test.shape[0]
        n_initial_features = initial_features_train.shape[1] if initial_features_train is not None else 0
        test_features = np.empty((n_test_samples, n_initial_features + len(extracted_patterns)), dtype=np.float32)
        test_features[:, :n_initial_features] = initial_features_test if initial_features_test is not None else 0.0
        
        for i, pattern in enumerate(extracted_patterns):
            input_series_idx = pattern_series_indices[i]
            start, width = pattern_starts[i], pattern_widths[i]
            
            # Extract the corresponding test input series data
            if n_input_series > 1:
                test_input_series = input_series_test[:, input_series_idx, :]
            else:
                test_input_series = input_series_test
            
            # Generate the same pattern feature for test data
            test_pattern_feature = calculate_pattern_rmse(test_input_series[:, start:start+width], pattern)
            test_features[:, n_initial_features+i] = test_pattern_feature
    
    # generate result dictionary
    result = {
        # Extracted patterns from input series
        'patterns': extracted_patterns, 
        'pattern_starts': pattern_starts, 
        'pattern_widths': pattern_widths,
        'pattern_series_indices': pattern_series_indices,
        
        # Feature set for ML model
        'train_features': train_features, 
        'test_features': test_features,
        'model': model
    }
    return result
