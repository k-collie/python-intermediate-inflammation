#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import argparse
import os

from inflammation import models, views
from inflammation.compute_data import analyse_data


def select_data_source(first_infile) -> models.AbstractDataSource:
    """
    Select a data source based on the first input file's extension
    """
    _, extension = os.path.splitext(first_infile)
    print(first_infile)
    if extension == '.json':
      return models.JSONDataSource(os.path.dirname(first_infile))
    elif extension == '.csv':
      return models.CSVDataSource(os.path.dirname(first_infile))
    else:
      raise ValueError(f'Unsupported data file format: {extension}')


def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    infiles = args.infiles
    if not isinstance(infiles, list):
        infiles = [args.infiles]


    if args.full_data_analysis:
        data_source = select_data_source(infiles[0])
        analyse_data(data_source)
        return

    for filename in infiles:
        inflammation_data = models.load_csv(filename)

        view_data = {
            'average': models.daily_mean(inflammation_data),
            'max': models.daily_max(inflammation_data),
            'min': models.daily_min(inflammation_data)
        }

        views.visualize(view_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient inflammation data management system')

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient')

    parser.add_argument(
        '--full-data-analysis',
        action='store_true',
        dest='full_data_analysis')

    args = parser.parse_args()

    main(args)
