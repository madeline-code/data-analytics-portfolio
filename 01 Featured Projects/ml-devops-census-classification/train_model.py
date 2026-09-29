import os

import pandas as pd
from sklearn.model_selection import train_test_split

from ml.data import process_data
from ml.model import (
    compute_model_metrics,
    inference,
    load_model,
    performance_on_categorical_slice,
    save_model,
    train_model,
)


project_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(project_path, "data", "census.csv")

# Load the Census data and remove spaces following CSV delimiters.
data = pd.read_csv(data_path, skipinitialspace=True)
data.columns = data.columns.str.strip()

# Split the data into training and testing datasets.
train, test = train_test_split(
    data,
    test_size=0.20,
    random_state=42,
    stratify=data["salary"],
)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

# Process the training and testing datasets.
X_train, y_train, encoder, lb = process_data(
    train,
    categorical_features=cat_features,
    label="salary",
    training=True,
)

X_test, y_test, _, _ = process_data(
    test,
    categorical_features=cat_features,
    label="salary",
    training=False,
    encoder=encoder,
    lb=lb,
)

# Train the classification model.
model = train_model(X_train, y_train)

# Save the model, categorical encoder, and label binarizer.
model_directory = os.path.join(project_path, "model")
os.makedirs(model_directory, exist_ok=True)

model_path = os.path.join(model_directory, "model.pkl")
encoder_path = os.path.join(model_directory, "encoder.pkl")
lb_path = os.path.join(model_directory, "lb.pkl")

save_model(model, model_path)
save_model(encoder, encoder_path)
save_model(lb, lb_path)

# Confirm that the saved model can be loaded.
model = load_model(model_path)

# Generate predictions for the test dataset.
preds = inference(model, X_test)

# Calculate and display overall model metrics.
precision, recall, fbeta = compute_model_metrics(y_test, preds)
print(
    f"Precision: {precision:.4f} | "
    f"Recall: {recall:.4f} | "
    f"F1: {fbeta:.4f}"
)

# Calculate performance for every value of every categorical feature.
slice_output_path = os.path.join(project_path, "slice_output.txt")

with open(slice_output_path, "w") as slice_file:
    for column_name in cat_features:
        for slice_value in sorted(test[column_name].unique()):
            count = test[test[column_name] == slice_value].shape[0]

            precision, recall, fbeta = performance_on_categorical_slice(
                test,
                column_name,
                slice_value,
                cat_features,
                "salary",
                encoder,
                lb,
                model,
            )

            print(
                f"{column_name}: {slice_value}, Count: {count:,}",
                file=slice_file,
            )
            print(
                f"Precision: {precision:.4f} | "
                f"Recall: {recall:.4f} | "
                f"F1: {fbeta:.4f}",
                file=slice_file,
            )

print(f"Model saved to {model_path}")
print(f"Encoder saved to {encoder_path}")
print(f"Slice metrics saved to {slice_output_path}")
