"""Logistic-regression models used in the A/B testing project."""

import pandas as pd
import statsmodels.api as sm


def prepare_page_model_data(df):
    """Create intercept and treatment indicator columns."""
    model_df = df.copy()
    model_df["intercept"] = 1
    model_df["ab_page"] = pd.get_dummies(model_df["group"])["treatment"].astype(int)
    X = model_df[["intercept", "ab_page"]]
    y = model_df["converted"]
    return model_df, X, y


def fit_page_model(df):
    """Fit conversion ~ treatment logistic regression."""
    _, X, y = prepare_page_model_data(df)
    return sm.Logit(y, X).fit()


def fit_page_country_model(df):
    """Fit conversion using treatment and country indicators."""
    model_df, _, y = prepare_page_model_data(df)
    country_dummies = pd.get_dummies(model_df["country"])
    model_df["US"] = country_dummies["US"].astype(int)
    model_df["UK"] = country_dummies["UK"].astype(int)
    X = model_df[["intercept", "ab_page", "US", "UK"]]
    return sm.Logit(y, X).fit()
