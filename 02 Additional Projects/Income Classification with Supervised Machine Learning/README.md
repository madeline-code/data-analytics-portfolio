# Income Classification with Supervised Machine Learning

A supervised machine learning project that uses U.S. Census data to predict whether an individual earns more than $50,000 per year.

The project was developed for a fictional charity, CharityML. The goal was to identify individuals who may be more likely to donate based on income classification. Several classification algorithms were compared before selecting and tuning the strongest model.

---

## Project Overview

This project covers the full supervised learning process, including:

- Data exploration
- Data preprocessing
- Feature transformation
- Model training
- Model comparison
- Hyperparameter tuning
- Model evaluation
- Feature importance analysis
- Feature reduction testing

The final model was a tuned Logistic Regression classifier.

---

## Machine Learning Models

Three supervised learning algorithms were evaluated:

### Decision Tree

Decision Trees were tested because they can model nonlinear relationships and provide interpretable classification rules.

### Random Forest

Random Forest was evaluated for its ability to combine multiple decision trees, reduce overfitting, and identify important predictive features.

### Logistic Regression

Logistic Regression produced the strongest combination of predictive performance and training efficiency and was selected as the final model.

---

## Model Evaluation

The models were evaluated using:

- Accuracy
- F0.5-score
- Training time
- Prediction time
- Performance across different training-set sizes

The F0.5-score was emphasized because the project placed greater weight on precision when identifying people predicted to earn more than $50,000.

### Naive Predictor

A baseline model that predicted every individual as earning more than $50,000 produced:

| Metric | Score |
|---|---:|
| Accuracy | 0.2478 |
| F0.5-score | 0.2917 |

---

## Final Model

Logistic Regression was selected as the final classifier.

GridSearchCV was used to tune the model's regularization parameter.

### Best Parameter

```text
C = 0.1
