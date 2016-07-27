from __future__ import print_function

import pandas as pd
import csv
import requests

def get_url(address):
    response = requests.get(address)
    if response.status_code != 200:
        return 'ValueError: Invalid Web Address'
    else:
        return response.status_code

def check_data(address):
    frame = url_to_df(address)
    if '&' in frame.iloc[1, 1]:
        return 'TypeError: URL cannot be made into csv'
    else:
        pass


def add(x, y):
    return x + y
#
# def url_to_csv(CSV_URL=None, name='csv_example'):
#     with requests.Session() as s:
#         download = s.get(CSV_URL)
#         decoded_content = download.content.decode('utf-8')
#         cr = csv.reader(decoded_content.splitlines(), delimiter=',')
#         my_list = list(cr)
#         title = "{}.csv".format(name)
#         outputFile = open(title, mode='w')
#         outputWriter = csv.writer(outputFile)
#         #print(len(my_list))
#         for row in my_list:
#             outputWriter.writerow(row)



def batch_url_to_csv(url_list, name_lst):
    title_lst = []
    new_name_lst = []
    for address, name in zip(url_list, name_lst):
        url_to_csv(address, name)
        new_name_lst.append(name)
    for f in new_name_lst:
        title = "{}.csv".format(f)
        title_lst.append(title)
    return title_lst

def url_to_df(url):
    frame= pd.read_csv(url)#, header=None)
    return frame

# def url_to_df(url):
#     response = urllib2.urlopen(url)
#     cr = csv.reader(response)
#     lst = []
#     for row in cr:
#         lst.append(row)
#     df = (pd.DataFrame(lst[1:], columns=lst[0]))
#     return df
#
# def url_to_df(url):
#     response = urllib2.urlopen(url)
#     cr = csv.reader(response)
#     lst = []
#     for row in cr:
#         lst.append(row)
#     df = pd.DataFrame(lst)
#     if 1 in df.columns:
#         df = (pd.DataFrame(lst[1:], columns=lst[0]))
#     return df
#

# url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
# s=requests.get(url).content
# c=pd.read_csv(io.StringIO(s.decode('utf-8')))

#
# CSV_URL = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv' #'http://google.com'#'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'#'http://google.com'#'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'#'http://samplescvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
# csv_lst = ['https://archive.ics.uci.edu/ml/machine-learning-databases/balloons/yellow-small.data',
#              'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv']
# file_ex = url_to_csv(CSV_URL, name='sacramento')
# df = url_to_df(CSV_URL)#, name='sacramento')
# print(df.head())
# fs = batch_url_to_csv(csv_lst, ['balloons', 'sacramento'])
# print(fs)
# # df = check_data('http://yahoo.com')
# # print(df)
#print('&' in df.iloc[1,1])
#print(df.iloc[1,1])





def url_to_csv(CSV_URL=None, name='csv_example'):
    try:
        response = requests.get(CSV_URL)
    except Exception:
        return ValueError

    if response.status_code < 400:
        with requests.Session() as s:
            download = s.get(CSV_URL)
            try:
                decoded_content = download.content.decode('utf-8')
            except UnicodeDecodeError:
                return TypeError
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            try:
                my_list = list(cr)
            except UnicodeDecodeError:
                return TypeError
            title = "{}.csv".format(name)
            outputFile = open(title, mode='w')
            outputWriter = csv.writer(outputFile)
            #print(len(my_list))
            for row in my_list:
                outputWriter.writerow(row)
    else:
        return ValueError
#
#
# def batch_url_to_csv(url_list, name_lst):
#     title_lst = []
#     new_name_lst = []
#     for address, name in zip(url_list, name_lst):
#         try:
#             url_to_csv(address, name)
#             new_name_lst.append(name)
#         except ValueError:# or ValueError:
#             return RuntimeWarning
#     for f in new_name_lst:
#         title = "{}.csv".format(f)
#         title_lst.append(title)
#     return title_lst
#
# def url_to_df(url):
#     frame= pd.read_csv(url, header=None)
#     return frame
