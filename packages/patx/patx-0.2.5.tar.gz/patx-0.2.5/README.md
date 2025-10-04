# PatX - Pattern eXtraction for Time Series Feature Engineering

[![PyPI version](https://badge.fury.io/py/patx.svg)](https://badge.fury.io/py/patx)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

PatX is a Python package for extracting polynomial patterns from time series data to create features for machine learning models. 
It uses Optuna optimization to automatically find patterns that work best for your target variable.

## Installation

```bash
pip install patx
```

## Quick Start

Copy and paste this complete example to get started immediately:

```python
import numpy as np
import pandas as pd
from patx import feature_extraction, load_remc_data
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

# Load the included REMC dataset with two input series (H3K4me3, H3K4me1)
data = load_remc_data(series=("H3K4me3", "H3K4me1"))
input_series = data['X_list']  # list of arrays, one per input series
y = data['y']
series_names = data['series_names']

print(f"Loaded {len(input_series)} input series: {series_names}")
print(f"Samples: {len(y)}, time points per input series: {input_series[0].shape[1]}")  # (1841, 40)

# Split data
indices = np.arange(len(y))
train_indices, test_indices = train_test_split(
    indices, test_size=0.2, random_state=42, stratify=y
)

# Use single input series as simple Pandas DataFrame (could also be 1D numpy array)
input_series_train = pd.DataFrame(input_series[0][train_indices])  # Simple DataFrame
input_series_test = pd.DataFrame(input_series[0][test_indices])    # Simple DataFrame
y_train, y_test = pd.Series(y[train_indices]), y[test_indices]

# Extract patterns and train model
result = feature_extraction(
    input_series_train=input_series_train, 
    y_train=y_train, 
    input_series_test=input_series_test, 
    n_trials=100, 
    show_progress=False
)

# Get results
trained_model = result['model']
patterns = result['patterns']
test_probabilities = trained_model.predict_proba(result['test_features'])

# Check performance
auc_score = roc_auc_score(y_test, test_probabilities)
print(f"\nResults:")
print(f"Found {len(patterns)} patterns from single input series")
print(f"Test AUC: {auc_score:.4f}")
print(f"Model features shape: {result['train_features'].shape}")  # (1177, 4)
```

### Multiple Input Series Example

For multiple input series data:

```python
# Use multiple input series as list of DataFrames
input_series_train_multiple = [pd.DataFrame(X[train_indices]) for X in input_series]
input_series_test_multiple = [pd.DataFrame(X[test_indices]) for X in input_series]

# Extract patterns from multiple input series
multiple_result = feature_extraction(
    input_series_train=input_series_train_multiple, 
    y_train=y_train, 
    input_series_test=input_series_test_multiple, 
    n_trials=50, 
    show_progress=False
)

# Check multiple input series results
multiple_probs = multiple_result['model'].predict_proba(multiple_result['test_features'])
multiple_auc = roc_auc_score(y_test, multiple_probs)
print(f"Multiple input series: {len(multiple_result['patterns'])} patterns, AUC={multiple_auc:.4f}")
print(f"Model features shape: {multiple_result['train_features'].shape}")  # (1177, 6)
```


### Input Data Types

PatX works with simple Pandas DataFrames or 1D numpy arrays:

```python
import pandas as pd
import numpy as np
from patx import feature_extraction

# Option 1: Simple Pandas DataFrame (recommended)
input_series_train = pd.DataFrame(your_data)  # Simple DataFrame
input_series_test = pd.DataFrame(your_test_data)  # Simple DataFrame

# Option 2: 1D numpy array (also works)
# input_series_train = np.array(your_data)  # 1D numpy array
# input_series_test = np.array(your_test_data)  # 1D numpy array

result = feature_extraction(
    input_series_train=input_series_train, 
    y_train=y_train, 
    input_series_test=input_series_test, 
    n_trials=100
)

# Check results
print(f"Found {len(result['patterns'])} patterns")
print(f"Pattern starts: {result['pattern_starts']}")
print(f"Pattern widths: {result['pattern_widths']}")
```

### Pattern Generation

PatX uses polynomial pattern generation by default. Patterns are automatically found using coefficients that work best for your data.

## API Reference

### feature_extraction

The main function for extracting patterns from input series data.

**Parameters:**
- `input_series_train`: Training input series data (simple DataFrame or 1D numpy array, or list for multiple input series)
- `y_train`: Training targets (Series or array)
- `input_series_test`: Test input series data (same structure as `input_series_train`)
- `initial_features`: Optional initial features (array or tuple of train/test arrays)
- `model`: Optional model instance (defaults to LightGBM based on task)
- `metric`: Optional; auto-detected (binary→auc, multiclass→accuracy, regression→rmse)
- `polynomial_degree`: Optional degree of polynomial patterns (default: 3)
- `val_size`: Optional validation split ratio (default: 0.2)
- `n_trials`: Maximum number of optimization trials (default: 300)
- `n_jobs`: Number of parallel jobs (default: -1)
- `show_progress`: Show progress bar (default: True)

**Returns:**
A dictionary containing:
- `patterns`: list of pattern arrays (just the pattern values)
- `pattern_starts`: start indices for each pattern
- `pattern_widths`: width of each pattern
- `pattern_series_indices`: which input series each pattern was extracted from
- `train_features`: training feature matrix for the ML model
- `test_features`: test feature matrix for the ML model
- `model`: the trained model

### Models

PatX works with any model that has `fit()`, `predict()`, and `predict_proba()` methods. Here's an example with XGBoost:

**XGBoost Example:**
```python
import xgboost as xgb

class XGBoostWrapper:
    def __init__(self, task_type='classification', n_classes=None):
        if task_type == 'classification':
            if n_classes == 2:
                self.model = xgb.XGBClassifier(random_state=42, eval_metric='auc')
            else:
                self.model = xgb.XGBClassifier(random_state=42, eval_metric='mlogloss')
        else:
            self.model = xgb.XGBRegressor(random_state=42, eval_metric='rmse')
    
    def fit(self, X_train, y_train, X_val=None, y_val=None):
        self.model.fit(X_train, y_train)
        return self
    
    def predict(self, X):
        return self.model.predict(X)
    
    def predict_proba(self, X):
        proba = self.model.predict_proba(X)
        # For binary classification, return only the positive class probabilities
        if proba.shape[1] == 2:
            return proba[:, 1]
        return proba
    
    def clone(self):
        return XGBoostWrapper('classification', 2)

# Use XGBoost model
model = XGBoostWrapper('classification', n_classes=2)
result = feature_extraction(input_series_train, y_train, input_series_test, model=model)
```

### Data

- `load_remc_data(series)`: Load the included REMC epigenomics dataset (multiple input series)

### Custom Models

You can use any model that has `fit()`, `predict()`, and `predict_proba()` methods. Here's an example with sklearn:

**Sklearn Classifier Example:**
```python
from sklearn.linear_model import LogisticRegression
from sklearn.base import clone

class SklearnClassifierWrapper:
    def __init__(self, sklearn_model):
        self.sklearn_model = sklearn_model
    
    def fit(self, X_train, y_train, X_val=None, y_val=None):
        self.sklearn_model.fit(X_train, y_train)
        return self
    
    def predict(self, X):
        return self.sklearn_model.predict(X)
    
    def predict_proba(self, X):
        return self.sklearn_model.predict_proba(X)
    
    def clone(self):
        return SklearnClassifierWrapper(clone(self.sklearn_model))

# Use custom model
model = SklearnClassifierWrapper(LogisticRegression())
result = feature_extraction(input_series_train, y_train, input_series_test, model=model)
```

This wrapper works with any sklearn classifier (RandomForest, SVM, etc.).

## Citation

If you use PatX in your research, please cite:

```bibtex
@software{patx,
  title={PatX: Pattern eXtraction for Time Series Feature Engineering},
  author={Wolber, J.},
  year={2025},
  url={https://github.com/Prgrmmrjns/patX}
}
```