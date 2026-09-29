"""Reusable data-quality helpers for the healthcare wrangling project."""

import pandas as pd


def missing_values(df):
    """Return missing-value counts by column."""
    return df.isna().sum().sort_values(ascending=False)


def duplicate_count(df):
    """Return the number of duplicated rows."""
    return int(df.duplicated().sum())


def numeric_summary(df):
    """Return descriptive statistics for numeric columns."""
    return df.describe(include="number")
