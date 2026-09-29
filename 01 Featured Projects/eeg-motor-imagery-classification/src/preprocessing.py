"""EEG data loading, preprocessing, and subject-level dataset construction."""
import numpy as np
import pandas as pd
import mne
from mne.datasets import eegbci

IMAGERY_RUNS = [4, 8, 12]

def download_subject_files(subjects, runs=IMAGERY_RUNS):
    return {s: eegbci.load_data(s, runs, update_path=False) for s in subjects}

def preprocess_subject(files):
    raws = [mne.io.read_raw_edf(f, preload=True, verbose=False) for f in files]
    raw = mne.concatenate_raws(raws)
    events, event_id = mne.events_from_annotations(raw, verbose=False)
    raw.filter(l_freq=8.0, h_freq=30.0, fir_design="firwin", verbose=False)
    imagery_event_id = {"left_hand": event_id["T1"], "right_hand": event_id["T2"]}
    return mne.Epochs(raw, events, event_id=imagery_event_id, tmin=0.0, tmax=4.0,
                      baseline=None, preload=True, reject_by_annotation=True, verbose=False)

def preprocess_subjects(subject_files):
    all_epochs, summary = {}, []
    for subject, files in subject_files.items():
        epochs = preprocess_subject(files)
        all_epochs[subject] = epochs
        left, right = len(epochs["left_hand"]), len(epochs["right_hand"])
        summary.append({"subject": subject, "left_trials": left, "right_trials": right,
                        "total_trials": left + right})
    return all_epochs, pd.DataFrame(summary)

def build_dataset(all_epochs):
    X_list, y_list, subject_ids = [], [], []
    for subject, epochs in all_epochs.items():
        X_subject = epochs.get_data()
        y_subject = np.where(epochs.events[:, 2] == epochs.event_id["left_hand"], 0, 1)
        X_list.append(X_subject); y_list.append(y_subject)
        subject_ids.extend([subject] * len(epochs))
    return np.concatenate(X_list), np.concatenate(y_list), np.asarray(subject_ids)
