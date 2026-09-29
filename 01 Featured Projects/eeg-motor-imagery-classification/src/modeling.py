"""Subject-level splitting, Random Forest training, and evaluation."""
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GroupShuffleSplit, GroupKFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from .feature_extraction import fit_csp

def subject_train_test_split(X, y, subject_ids, test_size=0.20, random_state=42):
    splitter = GroupShuffleSplit(n_splits=1, test_size=test_size, random_state=random_state)
    train_idx, test_idx = next(splitter.split(X, y, groups=subject_ids))
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx], subject_ids[train_idx], subject_ids[test_idx]

def train_random_forest(X_train, y_train):
    model = RandomForestClassifier(n_estimators=200, random_state=42, class_weight="balanced")
    model.fit(X_train, y_train)
    return model

def evaluate_model(y_true, y_pred):
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision_macro": precision_score(y_true, y_pred, average="macro"),
        "recall_macro": recall_score(y_true, y_pred, average="macro"),
        "f1_macro": f1_score(y_true, y_pred, average="macro"),
        "confusion_matrix": confusion_matrix(y_true, y_pred),
    }

def subject_level_cross_validation(X, y, subject_ids, n_splits=5):
    scores=[]
    for train_idx, test_idx in GroupKFold(n_splits=n_splits).split(X, y, groups=subject_ids):
        csp=fit_csp(X[train_idx], y[train_idx])
        Xtr, Xte=csp.transform(X[train_idx]), csp.transform(X[test_idx])
        model=train_random_forest(Xtr, y[train_idx])
        scores.append(accuracy_score(y[test_idx], model.predict(Xte)))
    return np.asarray(scores)
