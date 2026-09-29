"""Common Spatial Pattern (CSP) feature extraction."""
import contextlib
import io
from mne.decoding import CSP

def fit_csp(X_train, y_train, n_components=6):
    csp = CSP(n_components=n_components, reg=None, log=True, norm_trace=False)
    with contextlib.redirect_stdout(io.StringIO()):
        csp.fit(X_train, y_train)
    return csp

def transform_csp(csp, X_train, X_test):
    return csp.transform(X_train), csp.transform(X_test)
