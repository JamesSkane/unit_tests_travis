from pandas.io.common import CParserError
from urllib2 import HTTPError
from pandas.core.common import PandasError
import os
import pandas as pd
import numpy as np
import csv
import requests


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
        os.remove(name)
        raise TypeError('The url entered cannot be parsed into a csv.')
    return os.path.abspath(name)



def batch_url_to_csv(url_list, name_lst):
    """
    Raises a RuntimeWarning for bad URLs and/or urls that cannot be parsed into csv format.
    """

    title_lst = []
    new_name_lst = []
    for address, name in zip(url_list, name_lst):
        name = url_to_csv(address, name)
        new_name_lst.append(name)
    for f in new_name_lst:
        title = "{}.csv".format(f)
        title_lst.append(title)
    return title_lst



def url_to_df(url):
    """
    Raises RuntimeWarning if size of dataframe does not match the size of csv without headers,
    Also raises ValueError if invalid url passed as an argument.
    """

    try:
        frame = pd.read_csv(url, header=None)
        frame_length_pd = len(frame)
        frame_length_csv = len(pd.read_csv(url,header=None))#url_to_csv(url)
        if frame_length_pd == frame_length_csv:
            return frame
        else:
            raise RuntimeWarning('Number of rows in dataframe do not match the number of rows in csv when there is no header row in the csv.')
    except HTTPError:
        raise ValueError('The url entered cannot be parsed into a csv')

def add(x, y):
    return x + y







#url_to_csv('https://archive.ics.uci.edu/ml/machine-learning-databazes/car', 'cars')
#url_to_csv('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary')
#url_to_csv('https://www.yahoo.com/')
CSV_URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/balloons/yellow-small.data'#'https://archive.ics.uci.edu/ml/machine-learning-databases/car'
#csv_lst = ['https://archive.ics.uci.edu/ml/machine-learning-databases/balloons/yellow-small.data',
#             'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv']
#file_ex = url_to_csv(CSV_URL, name='sacramento')
fname=url_to_csv(CSV_URL, 'balloons')

print len(pd.read_csv(fname))
print len(url_to_df(CSV_URL))
#validate_csv('/Users/desert/unit_tests_travis/balloons.csv')
#df = url_to_df(CSV_URL)#, name='sacramento')
#print df.head()


#print(df.head())
#fs = batch_url_to_csv(csv_lst, ['balloons', 'sacramento'])




# def url_to_csv(CSV_URL=None, name='csv_example'):
#     with requests.Session() as s:
#         download = s.get(CSV_URL)
#         decoded_content = download.content.decode('utf-8')
#         cr = csv.reader(decoded_content.splitlines(), delimiter=',')
#         try:
#             my_list = list(cr)
#         except UnicodeDecodeError:
#             yield TypeError
#         title = "{}.csv".format(name)
#         outputFile = open(title, mode='w')
#         outputWriter = csv.writer(outputFile)
#         #print(len(my_list))
#         for row in my_list:
#             outputWriter.writerow(row)
#
#
# Direcory structure: does unittest discovery require __init__ and sub dir?
#df_rows = url_to_df('http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv')
#print df_rows
#
# def get_url(address):
#     """Called by url_to_csv, Raises a ValueError for bad URL """
#     response = requests.get(address)
#     if response.status_code != 200:
#         try:
#         # something
#         except ValueError as e:
#
#             # clean up
#             raise AssertionError('something went wrong')
#
#
#         else:
#             pass
#
#             # ck csv


# def get_url2(address):
#     """Called by url_to_csv, Raises a ValueError for bad URL """
#     response = requests.get(address)
#     if response.status_code != 200:
#         raise RuntimeWarning
#     else:
#         pass
#
#
# def url_to_csv2(url,name='csv_example'):
#     """Raises a TypeError for urls that cannot be parsed into csv format"""
#     get_url(url)
#     try:
#         frame = pd.read_csv(url, header=None)
#         return frame
#     except :
#         raise RuntimeWarning
#     except ZeroDivisionError:
#         raise