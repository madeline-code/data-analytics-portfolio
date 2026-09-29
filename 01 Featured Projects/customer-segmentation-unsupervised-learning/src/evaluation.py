"""Cluster-comparison helpers for the customer segmentation project."""

import pandas as pd


def cluster_distribution(labels, name="share"):
    """Return the percentage of observations assigned to each cluster."""
    values = pd.Series(labels).value_counts(normalize=True).sort_index() * 100
    return values.rename(name)


def compare_cluster_distributions(population_labels, customer_labels):
    """Compare customer and population cluster shares."""
    population = cluster_distribution(population_labels, "population_pct")
    customers = cluster_distribution(customer_labels, "customer_pct")
    comparison = pd.concat([population, customers], axis=1).fillna(0)
    comparison["difference_pct_points"] = (
        comparison["customer_pct"] - comparison["population_pct"]
    )
    return comparison
