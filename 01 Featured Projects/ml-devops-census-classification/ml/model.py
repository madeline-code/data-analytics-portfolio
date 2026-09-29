import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import fbeta_score, precision_score, recall_score

from ml.data import process_data


def train_model(X_train, y_train):
    """
    Train and return a random forest classification model.

    Inputs
    ------
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.

    Returns
    -------
    model
        Trained machine learning model.
    """
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model


def compute_model_metrics(y, preds):
    """
    Calculate precision, recall, and F1 score.

    Inputs
    ------
    y : np.array
        Known labels, binarized.
    preds : np.array
        Predicted labels, binarized.

    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """
    fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
    precision = precision_score(y, preds, zero_division=1)
    recall = recall_score(y, preds, zero_division=1)
    return precision, recall, fbeta


def inference(model, X):
    """
    Run model inference and return predictions.

    Inputs
    ------
    model
        Trained machine learning model.
    X : np.array
        Data used for prediction.

    Returns
    -------
    preds : np.array
        Predictions from the model.
    """
    return model.predict(X)


def save_model(model, path):
    """
    Serialize a model or encoder to a file.

    Inputs
    ------
    model
        Trained machine learning model or categorical encoder.
    path : str
        Path where the pickle file will be saved.
    """
    with open(path, "wb") as file:
        pickle.dump(model, file)


def load_model(path):
    """
    Load and return a serialized object.
    """
    with open(path, "rb") as file:
        return pickle.load(file)


def performance_on_categorical_slice(
    data,
    column_name,
    slice_value,
    categorical_features,
    label,
    encoder,
    lb,
    model,
):
    """
    Calculate model performance for one categorical data slice.

    Inputs
    ------
    data : pd.DataFrame
        Data containing the model features and label.
    column_name : str
        Categorical column used to select the slice.
    slice_value : str, int, float
        Value used to select the slice.
    categorical_features : list
        Names of the categorical features.
    label : str
        Name of the label column.
    encoder
        Fitted one-hot encoder.
    lb
        Fitted label binarizer.
    model
        Trained classification model.

    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """
    data_slice = data[data[column_name] == slice_value]

    X_slice, y_slice, _, _ = process_data(
        data_slice,
        categorical_features=categorical_features,
        label=label,
        training=False,
        encoder=encoder,
        lb=lb,
    )

    preds = inference(model, X_slice)
    precision, recall, fbeta = compute_model_metrics(y_slice, preds)

    return precision, recall, fbeta
