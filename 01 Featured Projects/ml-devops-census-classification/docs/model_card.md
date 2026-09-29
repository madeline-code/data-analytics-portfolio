# Model Card

For additional information, see the [Model Cards for Model Reporting paper](https://arxiv.org/pdf/1810.03993.pdf).

## Model Details

This project uses a random forest classifier from scikit-learn 1.3.2. The model was trained with a fixed random state of 42 to support reproducible results. Categorical variables were processed with one-hot encoding, and the salary label was processed with a label binarizer.

The model classifies Census records into two income categories: `<=50K` and `>50K`.

Developer: Madeline Galbraith

## Intended Use

The model was created as an educational machine-learning deployment project. It demonstrates data processing, binary classification, performance testing across categorical slices, model serialization, unit testing, and API deployment.

The model should not be used to make employment, lending, insurance, housing, or eligibility decisions about individuals.

## Training Data

The project uses the provided Census Income dataset. It contains 32,561 records and includes demographic, employment, education, financial, and household variables.

The data was divided using a stratified 80/20 train-test split. The training set contains 26,048 records. Eight categorical features were one-hot encoded:

- `workclass`
- `education`
- `marital-status`
- `occupation`
- `relationship`
- `race`
- `sex`
- `native-country`

The remaining numeric features were passed to the classifier without scaling. Spaces following CSV delimiters were removed during loading.

## Evaluation Data

The evaluation set contains 6,513 records, representing 20% of the supplied dataset. Stratification preserved the salary-class distribution during the split.

The fitted training encoder and label binarizer were applied to the evaluation data. Model performance was also calculated for each unique value within every categorical feature. Those results are stored in `slice_output.txt`.

## Metrics

The positive class is `>50K`. Performance was measured using precision, recall, and F1 score.

- Precision: **0.7353**
- Recall: **0.6378**
- F1 score: **0.6831**

Precision measures the share of predicted `>50K` records that were correct. Recall measures the share of actual `>50K` records detected by the model. F1 combines precision and recall into one score.

## Ethical Considerations

The dataset includes sensitive attributes, including race and sex. Patterns learned from historical Census records may reproduce social and economic disparities present in the source data. Performance can also vary across demographic and employment groups, as documented in `slice_output.txt`.

A salary classification can be harmful if treated as a measure of a person’s ability, value, or future earnings. Human review would not correct all risks created by using this model for decisions affecting individuals.

## Caveats and Recommendations

The model was trained on one supplied Census dataset and may not represent current populations or economic conditions. Some records contain unknown values represented by `?`, which the model treats as a categorical value.

The model has lower recall than precision, meaning it misses some records belonging to the `>50K` class. Slice-level results should be reviewed before any new use. Future work could compare additional classifiers, tune model parameters, evaluate class imbalance, and test performance on newer Census data.