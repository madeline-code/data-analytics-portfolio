"""Descriptive statistics used in the A/B testing project."""

def conversion_rate(df, group=None, country=None):
    """Return the mean conversion rate after optional filtering."""
    subset = df
    if group is not None:
        subset = subset[subset["group"] == group]
    if country is not None:
        subset = subset[subset["country"] == country]
    return subset["converted"].mean()


def country_counts(df):
    """Return the number of observations from each country."""
    return df["country"].value_counts()


def group_counts(df):
    """Return the number of observations in each experiment group."""
    return df["group"].value_counts()
