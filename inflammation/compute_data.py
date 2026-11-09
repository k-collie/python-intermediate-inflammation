"""Module containing mechanism for calculating standard deviation between datasets."""

import glob
import os
import pathlib
from collections.abc import Iterable

import numpy as np

from inflammation import models, views


def read_data(data_dir: pathlib.Path) -> Iterable[np.ndarray]:
    """
    Read a set of inflammation files from data_dir
    Return a set of numpy arrays containing the data
    """
    data_file_paths = glob.glob(os.path.join(data_dir, "inflammation*.csv"))
    if len(data_file_paths) == 0:
        raise ValueError(f"No inflammation data CSV files found in path {data_dir}")

    return map(models.load_csv, data_file_paths)


def analyse_data(data_dir):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""
    data = read_data(data_dir)

    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    graph_data = {
        "standard deviation by day": daily_standard_deviation,
    }
    views.visualize(graph_data)
