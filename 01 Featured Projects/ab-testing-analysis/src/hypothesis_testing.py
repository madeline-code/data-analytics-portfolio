"""Simulation-based hypothesis testing for conversion-rate differences."""

import numpy as np
import pandas as pd


def observed_difference(df):
    """Treatment conversion rate minus control conversion rate."""
    treatment = df.query('group == "treatment"')["converted"].mean()
    control = df.query('group == "control"')["converted"].mean()
    return treatment - control


def simulate_null_differences(df, iterations=500, random_state=None):
    """Simulate treatment-control differences under equal conversion rates."""
    rng = np.random.default_rng(random_state)
    p_null = df["converted"].mean()
    n_treatment = df.query('group == "treatment"').shape[0]
    n_control = df.query('group == "control"').shape[0]

    differences = []
    for _ in range(iterations):
        treatment = rng.choice(
            [0, 1], size=n_treatment, p=[1 - p_null, p_null]
        )
        control = rng.choice(
            [0, 1], size=n_control, p=[1 - p_null, p_null]
        )
        differences.append(treatment.mean() - control.mean())

    return np.asarray(differences)


def simulation_p_value(null_differences, observed_diff):
    """One-sided p-value used in the notebook."""
    return (pd.Series(null_differences) >= observed_diff).mean()
