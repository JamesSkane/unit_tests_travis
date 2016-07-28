import numpy as np
import requests, csv, unittest
from numpy.testing import assert_array_almost_equal
from requester import add, url_to_csv, get_url, url_to_df


class TestNumComponentsReturned(unittest.TestCase):


    def test_good_url(self):
        response = get_url('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data')
        self.assertEqual(response, None)

    def test_bad_url(self):
        with self.assertRaises(ValueError):
            url_to_csv('https://archive.ics.uci.edu/ml/machine-bearning-databases/car/')

    def test_url_to_csv_fails_csv_parse(self):
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/balloons'
        # url='http://www.yahoo.com'
        with self.assertRaises(TypeError):#, msg="URL cannot be parsed as CSV"):
            url_to_csv(url)


    def test_url_to_df_DataFrame_rows(self):
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data'
        df_rows = url_to_df(url).shape[0]
        with requests.Session() as s:
            download = s.get(url)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            csv_rows = len(my_list)
        self.assertEqual(df_rows, csv_rows)

    # def test_url_to_csv_invalid_url(self):
    #     url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.2_week.csv'
    #     with self.assertRaises(ValueError):
    #         url_to_csv(url, 'tmp.csv')

    def test_add(self):
        res = add(3, 4)
        self.assertEqual(res, 7)

    def test_add_fails_when_input_is_string(self):
        with self.assertRaises(TypeError):
            add(3, 'hello')

    def test_numpy_array_almost_equal(self):
        arr1 = np.array([0.0, 0.10000000, 0.15])
        arr2 = np.array([0.0, 0.10000089, 0.15])
        assert_array_almost_equal(arr1, arr2, decimal=6)





class TestSomeOtherThing(unittest.TestCase):

    def test_something_else(self):
        pass




if __name__ == '__main__':
    unittest.main(verbosity=20)