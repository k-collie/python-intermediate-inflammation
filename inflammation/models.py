"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains
inflammation data for a single patient taken over a number of days
and each column represents a single day across all patients.
"""

import glob
import os
from collections.abc import Iterable

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=",")


def daily_mean(data):
    """Calculate the daily mean of a 2d inflammation data array."""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2d inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2d inflammation data array."""
    return np.min(data, axis=0)


class CSVDataSource:
    """
    Loads all the inflammation CSV files within a specified directory.
    """

    def __init__(self, dir_path):
        self.dir_path = dir_path

    def load_inflammation_data(self) -> Iterable[np.ndarray]:
        data_file_paths = glob.glob(os.path.join(self.dir_path, "inflammation*.csv"))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation CSV files found in path {self.dir_path}")
        data = map(load_csv, data_file_paths)
        return list(data)
