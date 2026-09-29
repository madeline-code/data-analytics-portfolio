"""Plotting helper used in the medical appointment analysis."""

import matplotlib.pyplot as plt


def plot_bar(data, title, xlabel, ylabel):
    ax = data.plot(kind="bar", figsize=(8, 5))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=0)
    return ax
