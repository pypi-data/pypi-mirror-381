import lightgbm as lgb
from sklearn.metrics import accuracy_score, roc_auc_score, mean_squared_error
from sklearn.base import clone as sk_clone
import numpy as np

def get_lgb_params(task_type, n_classes=None):
    params = {
        'learning_rate': 0.1,
        'max_depth': 3,
        'num_iterations': 100,
        'random_state': 42,
        'num_threads': 1,   
        'force_col_wise': True,
        'verbosity': -1,
        'data_sample_strategy': 'goss',
    }
    if task_type == 'classification':
        if n_classes == 2:
            params['objective'] = 'binary'
            params['metric'] = 'auc'
        else:
            params['objective'] = 'multiclass'
            params['metric'] = 'multi_logloss'
            if n_classes is not None:
                params['num_class'] = n_classes
    else:
        params['objective'] = 'regression'
        params['metric'] = 'rmse'
    return params


class LightGBMModel:
    def __init__(self, params):
        self.params = params
        self.booster = None
    
    def clone(self):
        return LightGBMModel(self.params)
    
    def fit(self, X_train, y_train, X_val=None, y_val=None):
        train_data = lgb.Dataset(X_train, label=y_train)
        valid_sets = [lgb.Dataset(X_val, label=y_val, reference=train_data)] if X_val is not None and y_val is not None else []
        self.booster = lgb.train(self.params, train_data, valid_sets=valid_sets, callbacks=[lgb.early_stopping(10, verbose=False)] if valid_sets else None)
        return self
    
    def train(self, X_train, y_train, X_val=None, y_val=None):
        return self.fit(X_train, y_train, X_val, y_val)
    
    def predict(self, X):
        preds = self.booster.predict(X)
        if self.params.get('objective') == 'multiclass':
            return np.argmax(preds, axis=1)
        elif self.params.get('objective') == 'binary':
            return (preds > 0.5).astype(int)
        return preds
    
    def predict_proba(self, X):
        preds = self.booster.predict(X)
        return np.column_stack([1 - preds, preds]) if self.params.get('objective') == 'binary' else preds
    
    def predict_proba_positive(self, X):
        preds = self.predict_proba(X)
        return preds[:, 1] if preds.ndim == 2 else preds


def get_model(task_type='classification', n_classes=None):
    return LightGBMModel(get_lgb_params(task_type, n_classes))


def clone_model(model):
    clone_attr = getattr(model, 'clone', None)
    if callable(clone_attr):
        return clone_attr()
    return sk_clone(model) if hasattr(model, 'get_params') else model.__class__(model.params) if hasattr(model, 'params') else model

def evaluate_model_performance(model, X, y, metric):
    if metric == 'auc':
        y_pred = model.predict_proba(X) if len(np.unique(y)) > 2 else model.predict_proba_positive(X)
        return roc_auc_score(y, y_pred, multi_class='ovr', average='macro') if len(np.unique(y)) > 2 else roc_auc_score(y, y_pred)
    elif metric == 'accuracy':
        return accuracy_score(y, model.predict(X))
    elif metric == 'rmse':
        return np.sqrt(mean_squared_error(y, model.predict(X)))
