import numpy as np
from sklearn.preprocessing import LabelBinarizer, OneHotEncoder


def process_data(
    X,
    categorical_features=None,
    label=None,
    training=True,
    encoder=None,
    lb=None,
):
    """
    Process data for model training or inference.

    Categorical columns are one-hot encoded. Labels are converted into binary
    values when a label column is provided.

    Inputs
    ------
    X : pd.DataFrame
        Data containing the features and optional label.
    categorical_features : list[str]
        Names of the categorical features.
    label : str
        Name of the label column. If None, an empty label array is returned.
    training : bool
        Whether new encoders should be fitted.
    encoder
        Fitted OneHotEncoder used when training is False.
    lb
        Fitted LabelBinarizer used when training is False.

    Returns
    -------
    X : np.array
        Processed feature data.
    y : np.array
        Processed labels or an empty array.
    encoder
        Fitted or supplied OneHotEncoder.
    lb
        Fitted or supplied LabelBinarizer.
    """
    if categorical_features is None:
        categorical_features = []

    if label is not None:
        y = X[label]
        X = X.drop(columns=[label])
    else:
        y = np.array([])

    X_categorical = X[categorical_features].values
    X_continuous = X.drop(columns=categorical_features).values

    if training:
        encoder = OneHotEncoder(
            sparse_output=False,
            handle_unknown="ignore",
        )
        lb = LabelBinarizer()

        X_categorical = encoder.fit_transform(X_categorical)
        y = lb.fit_transform(y.values).ravel()
    else:
        X_categorical = encoder.transform(X_categorical)

        if label is not None:
            y = lb.transform(y.values).ravel()

    X_processed = np.concatenate(
        [X_continuous, X_categorical],
        axis=1,
    )

    return X_processed, y, encoder, lb


def apply_label(prediction):
    """
    Convert a binary prediction into its salary label.
    """
    if prediction[0] == 1:
        return ">50K"

    return "<=50K"
