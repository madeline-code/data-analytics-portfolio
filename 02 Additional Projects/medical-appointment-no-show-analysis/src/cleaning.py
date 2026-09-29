"""Data-cleaning helpers used in the medical appointment analysis."""

import pandas as pd


def prepare_appointments(df):
    """Prepare scheduling dates and calculate appointment wait time."""
    cleaned = df.copy()
    cleaned["ScheduledDay"] = pd.to_datetime(cleaned["ScheduledDay"])
    cleaned["AppointmentDay"] = pd.to_datetime(cleaned["AppointmentDay"])
    cleaned["WaitDays"] = (
        cleaned["AppointmentDay"].dt.normalize()
        - cleaned["ScheduledDay"].dt.normalize()
    ).dt.days
    return cleaned
