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
    frame= pd.read_csv(url, header=None)
    return frame


def url_to_csv(url,name='csv_example'):
    print 'hi'
    try:
        print 'hello'
        frame = pd.read_csv(url, header=None)
        print(frame.head())
        print url
        result = frame.to_csv(name)
        res = csv.reader(result.splitlines(), delimiter=',')
        return res
    except Exception:
        print 'bye'
        raise ValueError




# # import unittest
# #
# # def fun(x):
# #     return x + 1
# #
# # class MyTest(unittest.TestCase):
# #     def test(self):
# #         self.assertEqual(fun(3), 4)
# #
# #
# #
# # # if __name__ == '__main__':
# # #     unittest.main()
# import pandas as pd
#
# def url_to_df(url):
#     frame= pd.read_csv(url, header=None)
#     return frame
#
# def url_to_csv(url):
#     frame= pd.read_csv(url)
#     #frame.to_csv()
#
# df = url_to_df('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data')
# print df.head()
#
# import requests
#
# response = requests.get('http://google.com')
# print response.status_code < 400
# #assert response.status_code < 400

url_to_csv('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary')

