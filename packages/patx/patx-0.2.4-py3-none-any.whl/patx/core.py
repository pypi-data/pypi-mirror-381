"""
Core PatternOptimizer class for extracting polynomial patterns from time series data.
"""

import json
import os
from typing import Optional, Union, List, Dict, Tuple, Callable, Any
import numpy as np
import pandas as pd
from numpy.typing import NDArray
import matplotlib
matplotlib.use('Agg')
import optuna
from sklearn.model_selection import train_test_split

from .models import evaluate_model_performance, clone_model, get_model

optuna.logging.set_verbosity(optuna.logging.WARNING)

class PatternExtractor:
    """
    Extract polynomial patterns from time series data for feature engineering.
    
    This class uses Optuna optimization to find polynomial patterns in time series
    that are most predictive for the target variable.
    """
    
    def __init__(
        self, 
        X_train: Union[NDArray[np.float32], List[NDArray[np.float32]], pd.DataFrame, List[pd.DataFrame]], 
        y_train: Union[NDArray[np.float32], pd.Series], 
        X_test: Optional[Union[NDArray[np.float32], List[NDArray[np.float32]], pd.DataFrame, List[pd.DataFrame]]] = None,
        model: Optional[Any] = None,
        max_n_trials: Optional[int] = None, 
        n_jobs: Optional[int] = None, 
        show_progress: Optional[bool] = None,
        metric: Optional[str] = None, 
        polynomial_degree: Optional[int] = None,
        val_size: Optional[float] = None, 
        initial_features: Optional[Union[NDArray[np.float32], Tuple[NDArray[np.float32], NDArray[np.float32]]]] = None, 
        pattern_fn: Optional[Callable[[List[float], int], NDArray[np.float32]]] = None, 
        similarity_fn: Optional[Callable[[NDArray[np.float32], NDArray[np.float32]], NDArray[np.float32]]] = None
    ) -> None:
        """
        Initialize PatternExtractor.
        
        Parameters
        ----------
        X_train : array-like, DataFrame, or list
            Training data. If list, automatically handles multiple time series.
        y_train : array-like or Series
            Training targets
        X_test : array-like, DataFrame, or list, optional
            Test data for feature extraction (same structure as X_train)
        model : object, optional
            Model with fit() and predict() methods. Defaults to LightGBM.
        max_n_trials : int, optional
            Maximum number of optimization trials (default: 100)
        n_jobs : int, optional
            Number of parallel jobs for optimization (default: -1)
        show_progress : bool, optional
            Whether to show progress bar (default: True)
        metric : str, optional
            Evaluation metric ('rmse', 'accuracy', 'auc'). If None, inferred (default: None)
        polynomial_degree : int, optional
            Degree of polynomial patterns (default: 3)
        val_size : float, optional
            Validation size (default: 0.3)
        initial_features : array-like, optional
            Initial features to include
        pattern_fn : callable, optional
            Custom pattern creation function(coeffs, n_points). Defaults to polynomial_pattern.
        similarity_fn : callable, optional
            Custom similarity calculation function(X_region, pattern_values). Defaults to calculate_pattern_rmse.
        """
        # Convert pandas to numpy if needed
        def _to_numpy(x):
            if isinstance(x, (pd.DataFrame, pd.Series)):
                return x.values.astype(np.float32)
            return np.asarray(x, dtype=np.float32)
        
        # Auto-detect multiple series from X_train structure
        self.multiple_series = isinstance(X_train, list)

        # Normalize X_train into expected internal shape
        if self.multiple_series and isinstance(X_train, list):
            self.X_series_list = [_to_numpy(x) for x in X_train]
            self.X_train = np.stack(self.X_series_list, axis=1)
        else:
            self.X_series_list = None
            self.X_train = _to_numpy(X_train)

        self.y_train = _to_numpy(y_train)

        # Store X_test with new name
        self.X_test = X_test

        # Set defaults for optional parameters
        self.max_n_trials = max_n_trials if max_n_trials is not None else 100
        self.n_jobs = n_jobs if n_jobs is not None else -1
        self.show_progress = show_progress if show_progress is not None else True
        self.polynomial_degree = polynomial_degree if polynomial_degree is not None else 3
        self.val_size = val_size if val_size is not None else 0.3

        # Defaults for control params
        self.pattern_list = []
        self.pattern_starts = []
        self.pattern_ends = []
        self.pattern_series_indices = []
        # Determine task type and defaults
        unique_targets = np.unique(self.y_train)
        is_classification = unique_targets.size <= 20 and np.allclose(unique_targets, unique_targets.astype(int))
        if model is None:
            task_type = 'classification' if is_classification else 'regression'
            n_classes = int(unique_targets.size) if task_type == 'classification' else None
            self.model = get_model(task_type, n_classes=n_classes)
        else:
            self.model = model
        if metric is None:
            if is_classification:
                # Prefer AUC for binary problems, else accuracy
                self.metric = 'auc' if unique_targets.size == 2 else 'accuracy'
            else:
                self.metric = 'rmse'
        else:
            self.metric = metric
        self.features_list = []
        self.best_score = float('inf') if self.metric == 'rmse' else -float('inf')
        self.initial_features = initial_features
        self.pattern_fn = pattern_fn if pattern_fn is not None else self.polynomial_pattern
        self.similarity_fn = similarity_fn if similarity_fn is not None else self.calculate_pattern_rmse
    
    def __str__(self) -> str:
        """String representation of PatternExtractor."""
        n_patterns = len(self.pattern_list)
        series_info = f" ({len(self.X_series_list)} series)" if self.multiple_series else ""
        return f"PatternExtractor(patterns={n_patterns}{series_info}, metric='{self.metric}')"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (f"PatternExtractor(X_train={self.X_train.shape}, y_train={self.y_train.shape}, "
                f"patterns={len(self.pattern_list)}, metric='{self.metric}')")
    
    def __len__(self) -> int:
        """Return number of extracted patterns."""
        return len(self.pattern_list)
    
    def __getitem__(self, idx: int) -> Dict[str, Any]:
        """Get pattern by index."""
        if idx < 0 or idx >= len(self.pattern_list):
            raise IndexError(f"Pattern index {idx} out of range [0, {len(self.pattern_list)})")
        
        pattern_info = {
            'pattern': self.pattern_list[idx],
            'start': self.pattern_starts[idx],
            'end': self.pattern_ends[idx],
        }
        if self.multiple_series and self.pattern_series_indices:
            pattern_info['series_index'] = self.pattern_series_indices[idx]
        return pattern_info
    
    def __iter__(self):
        """Iterate over patterns."""
        for i in range(len(self.pattern_list)):
            yield self[i]
    
    @property
    def n_patterns(self) -> int:
        """Number of extracted patterns."""
        return len(self.pattern_list)
    
    @property
    def patterns(self) -> List[NDArray[np.float32]]:
        """List of all extracted patterns."""
        return self.pattern_list
    
    def polynomial_pattern(self, coeffs: List[float], n_points: int) -> NDArray[np.float32]:
        """Generate polynomial pattern from coefficients."""
        x = np.linspace(-1, 1, n_points, dtype=np.float32)
        coeffs = np.array(coeffs, dtype=np.float32)
        powers = np.arange(len(coeffs), dtype=np.float32)
        return np.sum(coeffs * (x[:, None] ** powers), axis=1)

    def calculate_pattern_rmse(self, X_region: NDArray[np.float32], pattern_values: NDArray[np.float32]) -> NDArray[np.float32]:
        """Calculate RMSE between data region and pattern."""
        return np.sqrt(np.mean((X_region - pattern_values) ** 2, axis=1))

    def objective(self, trial: optuna.Trial, dim: int) -> float:
        """Optuna objective function for pattern optimization."""
        series_index = trial.suggest_int('series_index', 0, self.X_train.shape[1] - 1) if self.multiple_series else None
        pattern_start = trial.suggest_int('pattern_start', 0, dim - 2)
        pattern_width = trial.suggest_int('pattern_width', 1, dim - pattern_start)
        coeffs = [trial.suggest_float(f'c{i}', -1, 1) for i in range(self.polynomial_degree + 1)]
        X_data = self.X_train[:, series_index, :] if self.multiple_series and series_index is not None and self.X_train.ndim == 3 else self.X_train
        X_region = X_data[:, pattern_start:pattern_start + pattern_width]
        new_feature = self.similarity_fn(X_region, self.pattern_fn(coeffs, pattern_width))
        X_combined = np.column_stack(self.features_list + [new_feature]) if self.features_list else new_feature.reshape(-1, 1)
        X_train, X_val, y_train, y_val = train_test_split(X_combined, self.y_train, test_size=self.val_size, random_state=42)
        model = clone_model(self.model)
        
        model.fit(X_train, y_train, X_val, y_val)
        return evaluate_model_performance(model, X_val, y_val, self.metric)
    
    def feature_extraction(self, X_series_list: Optional[List[NDArray[np.float32]]] = None) -> Dict[str, Any]:
        """
        Extract features using optimized polynomial patterns.
        
        Parameters
        ----------
        X_series_list : list, optional
            List of time series data
            
        Returns
        -------
        dict
            Dictionary containing patterns, features, and model results
        """
        first_pattern = True
        if X_series_list is not None and self.multiple_series:
            self.X_series_list = [np.asarray(x, dtype=np.float32) for x in X_series_list]
            self.X_train = np.stack(self.X_series_list, axis=1)
        dim = self.X_train.shape[2] if self.multiple_series and self.X_train.ndim == 3 else self.X_train.shape[1]
        train_initial_features, test_initial_features = (None, None) if self.initial_features is None else ((np.asarray(self.initial_features[0], dtype=np.float32), np.asarray(self.initial_features[1], dtype=np.float32)) if isinstance(self.initial_features, tuple) and len(self.initial_features) == 2 else (np.asarray(self.initial_features, dtype=np.float32), None))
        if train_initial_features is not None: 
            self.features_list = [train_initial_features]
        
        while True:
            study = optuna.create_study(direction="minimize" if self.metric == 'rmse' else "maximize", pruner=optuna.pruners.MedianPruner())
            study.optimize(lambda trial: self.objective(trial, dim), n_trials=self.max_n_trials, n_jobs=self.n_jobs, show_progress_bar=self.show_progress)
            if first_pattern or (self.metric == 'rmse' and study.best_value < self.best_score) or (self.metric != 'rmse' and study.best_value > self.best_score):
                self.best_score = study.best_value
                best_params = study.best_trial.params
                pattern_start = best_params['pattern_start']
                pattern_width = best_params['pattern_width']
                coeffs = [best_params[f'c{i}'] for i in range(self.polynomial_degree + 1)]
                series_index = best_params.get('series_index')
                pattern_values = self.pattern_fn(coeffs, pattern_width)
                pattern_end = pattern_start + pattern_width
                new_pattern = np.zeros(dim, dtype=np.float32)
                new_pattern[pattern_start:pattern_end] = pattern_values
                self.pattern_list.append(new_pattern)
                self.pattern_starts.append(pattern_start)
                self.pattern_ends.append(pattern_end)
                if self.multiple_series:
                    self.pattern_series_indices.append(series_index)
                X_data = self.X_train
                if self.multiple_series and series_index is not None and X_data.ndim == 3:
                    X_data = X_data[:, series_index, :]
                X_region = X_data[:, pattern_start:pattern_end]
                new_feature_full = self.similarity_fn(X_region, pattern_values)
                self.features_list.append(new_feature_full)
                first_pattern = False
            else:
                break
        
        cached_features = np.column_stack(self.features_list) if self.features_list else np.empty((self.X_train.shape[0], 0))
        X_train, X_val, y_train, y_val = train_test_split(cached_features, self.y_train, test_size=self.val_size, random_state=42)
        self.model.fit(X_train, y_train, X_val, y_val)
        n_test_samples = self.X_test[0].shape[0] if isinstance(self.X_test, list) else self.X_test.shape[0]
        n_pattern_features = len(self.pattern_list)
        n_initial_features = train_initial_features.shape[1] if train_initial_features is not None else 0
        X_test = np.empty((n_test_samples, n_initial_features + n_pattern_features), dtype=np.float32)
        X_test[:, :n_initial_features] = test_initial_features if test_initial_features is not None else 0.0
        for i, pattern in enumerate(self.pattern_list):
            series_idx = self.pattern_series_indices[i] if self.multiple_series and self.pattern_series_indices else None
            X_for_pattern = self.X_test[series_idx] if self.multiple_series and isinstance(self.X_test, list) and series_idx is not None else self.X_test
            X_data = np.asarray(X_for_pattern, dtype=np.float32) if not isinstance(X_for_pattern, np.ndarray) else X_for_pattern
            if self.multiple_series and series_idx is not None and X_data.ndim == 3:
                X_data = X_data[:, series_idx, :]
            start, end = self.pattern_starts[i], self.pattern_ends[i]
            X_region = X_data[:, start:end]
            pattern_feature = self.similarity_fn(X_region, pattern[start:end]).reshape(-1, 1)
            X_test[:, n_initial_features + i:n_initial_features + i+1] = pattern_feature
        result = {'patterns': self.pattern_list,'starts': self.pattern_starts,'ends': self.pattern_ends,'features': cached_features,'X_train': X_train,'X_val': X_val,'y_train': y_train,'y_val': y_val,'X_test': X_test}
        if self.multiple_series and self.pattern_series_indices: 
            result['series_indices'] = self.pattern_series_indices
        X_combined = np.vstack((X_train, X_val))
        y_combined = np.hstack((y_train, y_val))
        X_train, X_val, y_train, y_val = train_test_split(X_combined, y_combined, test_size=self.val_size, random_state=42)
        self.model.fit(X_train, y_train, X_val, y_val)
        result['model'] = self.model
        return result

    def save_parameters_to_json(self, name: str = 'patterns') -> None:
        """
        Save all optimized pattern parameters to a JSON file.
        
        Parameters
        ----------
        name : str, optional
            Name for file organization (default: 'patterns')
        """
        params_dict = {
            'metric': self.metric,
            'polynomial_degree': self.polynomial_degree,
            'n_patterns': len(self.pattern_list),
            'patterns': []
        }
        for i, pattern in enumerate(self.pattern_list):
            pattern_info = {
                'pattern_id': i,
                'pattern_start': int(self.pattern_starts[i]),
                'pattern_width': int(self.pattern_ends[i] - self.pattern_starts[i]),
                'pattern_values': pattern[self.pattern_starts[i]:self.pattern_ends[i]].tolist(),
            }
            if self.multiple_series and self.pattern_series_indices:
                pattern_info['series_index'] = int(self.pattern_series_indices[i])
            params_dict['patterns'].append(pattern_info)
        
        os.makedirs(f'json_files/{name}', exist_ok=True)
        with open(f'json_files/{name}/pattern_parameters.json', 'w') as f:
            json.dump(params_dict, f, indent=2)
