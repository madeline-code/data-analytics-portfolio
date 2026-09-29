"""Analysis helpers used in the medical appointment no-show project."""

import numpy as np
import pandas as pd


def average_wait_by_status(df):
    return df.groupby("No-show")["WaitDays"].mean()


def sms_attendance_percentages(df):
    result = pd.crosstab(
        df["SMS_received"],
        df["No-show"],
        normalize="index"
    ) * 100
    return np.round(result, 2)


def average_age_by_status(df):
    return df.groupby("No-show")["Age"].mean()
