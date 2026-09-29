"""Plotting helpers used in the A/B testing project."""

import matplotlib.pyplot as plt


def plot_country_visits(df):
    ax = df["country"].value_counts().plot(kind="bar")
    ax.set_title("Number of Visits From Each Country")
    ax.set_ylabel("Count of Visits")
    return ax


def plot_null_distribution(differences, bins=30):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(differences, bins=bins)
    ax.set_xlabel("Difference in Conversion Rates")
    ax.set_ylabel("Frequency")
    ax.set_title("Simulated Differences Under the Null Hypothesis")
    return ax
