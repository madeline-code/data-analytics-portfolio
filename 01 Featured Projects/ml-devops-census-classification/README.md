# Census Income Classification ML Pipeline

## Project Overview

This project builds and serves a machine-learning pipeline that predicts whether a Census record belongs to the `<=50K` or `>50K` income category.

The project covers preprocessing, model training, serialization, performance testing across demographic slices, automated tests, continuous integration, and inference through a FastAPI service.

## Technologies Used

- Python
- pandas
- NumPy
- scikit-learn
- Random Forest
- FastAPI
- Pydantic
- pytest
- Flake8
- GitHub Actions
- Pickle model serialization

## Dataset

The supplied Census Income dataset contains **32,561 records** with demographic, employment, education, financial, and household variables.

The pipeline uses a stratified **80/20 train-test split** with `random_state=42`.

Categorical variables are transformed with one-hot encoding. The salary label is converted to a binary target using `LabelBinarizer`.

## Machine Learning Pipeline

### Data Processing

`ml/data.py` contains reusable preprocessing functions.

The pipeline:

- Separates categorical and continuous features
- One-hot encodes categorical variables
- Handles unseen categories during inference
- Binarizes the salary label
- Reuses the fitted encoder for test data and API predictions

### Model Training

A `RandomForestClassifier` is trained to predict the income category.

The trained classifier, categorical encoder, and label binarizer are serialized so the same fitted preprocessing and model objects can be reused.

## Model Performance

The positive class is `>50K`.

| Metric | Result |
|---|---:|
| Precision | **0.7353** |
| Recall | **0.6378** |
| F1 Score | **0.6831** |

Precision measures the share of predicted `>50K` records that were correct. Recall measures the share of actual `>50K` records detected by the classifier.

## Slice Performance

Model performance is also evaluated separately for every value of each categorical feature.

The project records precision, recall, and F1 for slices across:

- Work class
- Education
- Marital status
- Occupation
- Relationship
- Race
- Sex
- Native country

The generated results are stored in `slice_output.txt`.

This makes it possible to inspect model behavior across population subgroups rather than relying only on aggregate performance.

## FastAPI Service

`main.py` exposes the trained model through a FastAPI application.

### Health Endpoint

```http
GET /
```

Returns a welcome response confirming that the API is running.

### Prediction Endpoint

```http
POST /data/
```

Accepts one Census record and returns its predicted salary category.

Example response:

```json
{
  "result": ">50K"
}
```

Pydantic validates the incoming fields before the record is passed through the fitted encoder and classifier.

## Automated Testing

The project includes pytest tests covering:

- Random Forest model creation
- Prediction output shape
- Precision, recall, and F1 calculations
- Conversion of binary predictions to readable salary labels

## Continuous Integration

The included GitHub Actions workflow runs code-quality checks and automated tests after pushes.

The CI process uses:

- Flake8
- pytest

This provides an automated check that the pipeline continues to pass its tests as the code changes.

## Project Structure

```text
ml-devops-census-classification/
│
├── README.md
├── main.py
├── train_model.py
├── local_api.py
├── slice_output.txt
├── requirements.txt
│
├── ml/
│   ├── __init__.py
│   ├── data.py
│   └── model.py
│
├── tests/
│   └── test_ml.py
│
├── data/
│   └── census.csv
│
├── model/
│   ├── model.pkl
│   ├── encoder.pkl
│   └── lb.pkl
│
└── .github/
    └── workflows/
        └── main.yml
```

## Running the Project

Install the dependencies:

```bash
pip install -r requirements.txt
```

Train the model and generate slice metrics:

```bash
python train_model.py
```

Start the FastAPI application:

```bash
uvicorn main:app --reload
```

Run the automated tests:

```bash
pytest tests/test_ml.py -v
```

Test the local API from another terminal:

```bash
python local_api.py
```

## Skills Demonstrated

- Machine-learning pipeline development
- Binary classification
- Random Forest modeling
- Categorical feature encoding
- Model serialization
- Model inference
- Performance metrics
- Categorical slice evaluation
- REST API development
- FastAPI
- Pydantic validation
- Unit testing
- Continuous integration
- GitHub Actions
- Production-style project organization
