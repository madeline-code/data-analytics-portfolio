"""Analysis helpers for the cleaned CMS and Census dataset."""

def correlation_table(df, columns):
    """Return a correlation matrix for selected numeric columns."""
    return df[columns].corr(numeric_only=True)


def grouped_summary(df, group_col, value_col):
    """Return count, mean, median, and standard deviation by group."""
    return df.groupby(group_col)[value_col].agg(["count", "mean", "median", "std"])
