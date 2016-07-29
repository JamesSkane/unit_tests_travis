from urllib2 import HTTPError
import os
import pandas as pd
import numpy as np
import csv
import requests
import warnings
from collections import Counter


def get_url(address):
    """
    Called by url_to_csv, Raises a ValueError for bad URL
     """

    response = requests.get(address)
    if response.status_code != 200:
        raise ValueError('The url entered does not exist. Must enter valid url.')
    else:
        pass

def validate_csv(csv_file):
    """
    Checks that the csv file being created is not html
    """

    frame = pd.read_csv(csv_file)
    cols = frame.columns.tolist()
    for i in range(len(cols)):
        series = frame[cols[i]].astype(str)
        if np.any(series.str.contains('html')):
            os.remove(csv_file)
            raise RuntimeWarning('URL address is not in csv format, column %i contains html.' % i)
        else:
            pass


def url_to_csv(url,name='csv_example'):
    """
    Raises a TypeError for urls that cannot be parsed into csv format
    """

    get_url(url)
    try:
        frame = pd.read_csv(url, header=None)
        name = "{}.csv".format(name)
        frame.to_csv(name)
        validate_csv(url)
    except Exception:
        if os.path.exists(name):
            os.remove(name)
        raise TypeError('The url entered cannot be parsed into a csv.')
    return os.path.abspath(name)



def batch_url_to_csv(url_list, name_lst):
    """
    Raises a RuntimeWarning for bad URLs and/or urls that cannot be parsed into csv format.
    """

    title_lst = []
    duplicates = [val > 1 for val in Counter(url_list).values()]
    if True in duplicates:
        raise AssertionError("Duplicate URLs cannot be present in the parameter 'urls'.")
    for address, name in zip(url_list, name_lst):
        try:
            name = url_to_csv(address, name)
            title_lst.append(name)
        except Exception:
            warnings.warn("URL was skipped, not a valid url.", RuntimeWarning)
    return title_lst



def url_to_df(url):
    """
    Raises RuntimeWarning if size of dataframe does not match the size of csv without headers,
    Also raises ValueError if invalid url passed as an argument.
    """

    try:
        frame = pd.read_csv(url, header=None)
        frame_length_pd = len(frame)
        frame_length_csv = len(pd.read_csv(url,header=None))
        if frame_length_pd == frame_length_csv:
            return frame
        else:
            raise RuntimeWarning('Number of rows in dataframe do not match the number of rows in csv when there is no header row in the csv.')
    except HTTPError:
        raise ValueError('The url entered cannot be parsed into a csv')
