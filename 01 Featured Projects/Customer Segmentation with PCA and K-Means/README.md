# Customer Segmentation with PCA and K-Means

An unsupervised machine learning project that analyzes demographic data from the German population and customers of a mail-order company to identify customer groups with distinct demographic characteristics.

The analysis uses data provided by Bertelsmann Arvato Analytics and was completed as part of Udacity coursework.

---

## Project Overview

The project compares the general population of Germany with customers of a mail-order company.

The workflow includes:

- Data cleaning
- Missing-value analysis
- Categorical encoding
- Feature engineering
- Median imputation
- Feature scaling
- Principal Component Analysis (PCA)
- K-Means clustering
- Customer segment comparison
- Cluster interpretation

The final analysis identifies population groups that appear much more frequently among the company's customers.

---

## Dataset

The general population dataset contained:

- **891,221 people**
- **85 original features**

The customer dataset contained:

- **191,652 customers**
- **85 original features**

The demographic variables include information related to:

- Age
- Income
- Wealth
- Household characteristics
- Financial behavior
- Residential characteristics
- Consumer characteristics
- Personal and social characteristics

---

## Data Cleaning

Missing and unknown values were first converted to `NaN` using the supplied feature information.

Six columns with unusually high levels of missing data were removed:

- `TITEL_KZ`
- `AGER_TYP`
- `KK_KUNDENTYP`
- `KBA05_BAUMAX`
- `GEBURTSJAHR`
- `ALTER_HH`

Rows containing more than 20 missing values were also removed from the primary population dataset.

This left:

**797,426 population records**

for the machine learning analysis.

---

## Feature Engineering

Categorical variables were converted into numerical features so they could be used by the machine learning models.

Binary categorical variables were retained or recoded when needed.

Multi-level categorical variables were converted into dummy variables using `pd.get_dummies()`.

Two mixed demographic variables were separated into new features.

### PRAEGENDE_JUGENDJAHRE

Converted into:

- `PRAEGENDE_DECADE`
- `PRAEGENDE_MOVEMENT`

### CAMEO_INTL_2015

Converted into:

- `CAMEO_WEALTH`
- `CAMEO_LIFESTAGE`

Several remaining mixed variables were removed rather than re-encoded.

After preprocessing and feature engineering, the dataset contained:

**192 features**

---

## Missing Value Imputation

Remaining missing values were replaced using median imputation.

Median imputation allowed retained records to remain in the analysis without giving extreme values excessive influence.

After imputation:

- **797,426 rows remained**
- **192 features remained**
- **No missing values remained**

---

## Feature Scaling

The features had different numerical ranges, so `StandardScaler` was used before PCA.

After scaling, the features were centered near:

- Mean: **0**
- Standard deviation: **1**

The fitted preprocessing objects were retained and later applied to the customer dataset.

---

## Principal Component Analysis

PCA was used to reduce the number of features before clustering.

The cumulative explained variance was examined across several component counts:

| Principal Components | Variance Explained |
|---:|---:|
| 20 | 40.34% |
| 40 | 55.68% |
| 60 | 66.87% |
| 80 | ~77% |
| 96 | 85.37% |

The final PCA model retained:

**80 principal components**

These components preserved approximately:

**77.11% of the total variance**

This reduced the dataset from **192 features to 80 components** before clustering.

---

## Interpreting the Principal Components

The first three principal components captured several major demographic patterns.

### Principal Component 1

PC1 was strongly associated with socioeconomic and residential characteristics.

Higher values were associated with:

- Higher income
- Greater wealth
- Higher socioeconomic status
- Residential areas containing larger homes

Lower values were associated with:

- Financial minimalism
- Lower socioeconomic measures
- Residential areas containing more small buildings

### Principal Component 2

PC2 separated groups based largely on:

- Age
- Saving behavior
- Investment behavior
- Financial preparedness
- Lifestyle characteristics

### Principal Component 3

PC3 was strongly associated with:

- Personality characteristics
- Social characteristics
- Gender coding

---

## K-Means Clustering

K-Means models were tested using cluster counts from **2 through 10**.

Average within-cluster distance decreased as the number of clusters increased.

The improvement began to level off near six clusters, so the final model used:

**6 clusters**

The 797,426 population records were distributed as follows:

| Cluster | Population |
|---:|---:|
| 0 | 160,820 |
| 1 | 117,675 |
| 2 | 196,587 |
| 3 | 113,049 |
| 4 | 88,398 |
| 5 | 120,897 |

---

## Applying the Model to Customers

The same cleaning, encoding, imputation, scaling, PCA, and clustering transformations were applied to the customer dataset.

The customer models were not refit. The transformations learned from the general population were reused so the two groups could be compared directly.

After preprocessing:

- **141,640 customer records remained**
- **192 features were produced**
- PCA reduced the data to **80 components**

Customer cluster assignments were:

| Cluster | Customers |
|---:|---:|
| 0 | 38,643 |
| 1 | 63,416 |
| 2 | 30,263 |
| 3 | 1,840 |
| 4 | 2,185 |
| 5 | 5,293 |

---

## Customer Segment Comparison

The customer distribution differed substantially from the general German population.

| Cluster | General Population | Customers | Difference |
|---:|---:|---:|---:|
| 0 | 20.17% | 27.28% | +7.12% |
| 1 | 14.76% | **44.77%** | **+30.02%** |
| 2 | 24.65% | 21.37% | -3.29% |
| 3 | 14.18% | **1.30%** | **-12.88%** |
| 4 | 11.09% | 1.54% | -9.54% |
| 5 | 15.16% | 3.74% | -11.42% |

Cluster 1 was the strongest customer group.

It represented only about **14.76% of the general population**, yet accounted for approximately **44.77% of customers**.

---

## Strongest Customer Segment

### Cluster 1

Cluster 1 was highly overrepresented among customers.

The reconstructed cluster center suggested characteristics associated with:

- Lower income measures
- Lower wealth measures
- Stronger financial-minimalist characteristics
- Lower saving tendencies
- Older age categories
- Generational characteristics centered near the 1960s–1970s

This group appears to represent one of the company's strongest customer segments.

---

## Most Underrepresented Segment

### Cluster 3

Cluster 3 accounted for:

- **14.18% of the general population**
- Only **1.30% of customers**

Its reconstructed cluster center showed characteristics associated with:

- Higher income
- Greater wealth
- Strong saving tendencies
- Lower financial-minimalist characteristics
- Younger age categories

This segment appears much less likely to belong to the company's existing customer base.

---

## Key Result

The clustering analysis showed that the company's customers are not distributed evenly across the German population.

The strongest difference occurred in **Cluster 1**:

**14.76% of the general population → 44.77% of customers**

This represents an increase of approximately:

**30 percentage points**

The result identifies a demographic group that could receive greater attention when selecting audiences for future marketing campaigns.

---

## Skills Demonstrated

- Python
- Pandas
- NumPy
- scikit-learn
- Unsupervised Machine Learning
- Principal Component Analysis
- K-Means Clustering
- Customer Segmentation
- Dimensionality Reduction
- Feature Engineering
- One-Hot Encoding
- Missing Value Analysis
- Median Imputation
- StandardScaler
- Data Cleaning
- Data Wrangling
- Cluster Analysis
- Demographic Analysis
- Data Visualization

---

## Files

- `Identify_Customer_Segments.ipynb` — Jupyter Notebook containing the complete analysis
- `Identify_Customer_Segments.html` — HTML version of the completed notebook

---

## Portfolio

[Return to Data Analytics Portfolio](../README.md)
