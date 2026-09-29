# Census Income Classification API

This project trains a machine-learning model on publicly available Census Income data and serves predictions through a FastAPI application. It includes categorical-slice monitoring, automated tests, code-quality checks, serialized model files, and a local API client.

## Repository

Public GitHub repository:

[https://github.com/madeline-code/Deploying-a-Scalable-ML-Pipeline-with-FastAPI](https://github.com/madeline-code/Deploying-a-Scalable-ML-Pipeline-with-FastAPI)

## Project Results

The random forest classifier predicts whether a Census record belongs to the `<=50K` or `>50K` income category.

| Metric | Score |
|---|---:|
| Precision | 0.7353 |
| Recall | 0.6378 |
| F1 score | 0.6831 |

Performance for every unique value within each categorical feature is recorded in `slice_output.txt`.

## Data

The supplied Census Income dataset contains 32,561 records. The pipeline removes spaces following CSV delimiters and uses a stratified 80/20 train-test split.

The following categorical features are one-hot encoded:

- `workclass`
- `education`
- `marital-status`
- `occupation`
- `relationship`
- `race`
- `sex`
- `native-country`

The salary label is converted into binary values using `LabelBinarizer`.

## Model

The project uses `RandomForestClassifier` from scikit-learn. A fixed random state of 42 supports repeatable training results.

The training pipeline saves:

- `model/model.pkl`
- `model/encoder.pkl`
- `model/lb.pkl`
- `slice_output.txt`

Additional model information appears in `model_card.md`.

## Project Files

- `data/census.csv`: Census Income dataset
- `ml/data.py`: preprocessing and label conversion
- `ml/model.py`: training, inference, metrics, serialization, and slice testing
- `train_model.py`: training pipeline
- `test_ml.py`: unit tests
- `main.py`: FastAPI application
- `local_api.py`: local GET and POST request client
- `model_card.md`: model documentation
- `slice_output.txt`: categorical-slice performance
- `.github/workflows/manual.yml`: GitHub Actions workflow
- `screenshots/`: required verification images

## Local Setup

Python 3.8.10 was used during development.

Create and activate a virtual environment on Windows:

```powershell
py -3.8 -m venv fastapi
.\fastapi\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Install Flake8 for local code-quality checks:

```powershell
python -m pip install flake8
```

## Train the Model

Run:

```powershell
python train_model.py
```

The command trains the classifier, prints the evaluation metrics, saves the fitted model and encoders, and writes categorical-slice results to `slice_output.txt`.

## Run the Tests

```powershell
python -m pytest test_ml.py -v
```

The test suite checks:

- The algorithm returned by `train_model`
- The prediction type and shape returned by `inference`
- The calculated precision, recall, and F1 values
- The conversion of binary predictions into salary labels

## Run Flake8

```powershell
flake8 . --count --max-line-length=88 --statistics --exclude=.venv,fastapi,.idea
```

GitHub Actions runs Flake8 and pytest after every push.

## Run the API

Start the FastAPI server:

```powershell
uvicorn main:app --reload
```

The application runs at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### GET `/`

Returns the welcome message:

```json
{
  "message": "Hello from the API!"
}
```

### POST `/data/`

Accepts one Census record and returns its predicted salary category.

Sample request:

```json
{
  "age": 37,
  "workclass": "Private",
  "fnlgt": 178356,
  "education": "HS-grad",
  "education-num": 10,
  "marital-status": "Married-civ-spouse",
  "occupation": "Prof-specialty",
  "relationship": "Husband",
  "race": "White",
  "sex": "Male",
  "capital-gain": 0,
  "capital-loss": 0,
  "hours-per-week": 40,
  "native-country": "United-States"
}
```

Sample response:

```json
{
  "result": "<=50K"
}
```

## Test the API Client

Keep the FastAPI server running in one terminal. Open another terminal and run:

```powershell
python local_api.py
```

Expected output:

```text
Status Code: 200
Result: Hello from the API!
Status Code: 200
Result: <=50K
```

## Author

Madeline Galbraith