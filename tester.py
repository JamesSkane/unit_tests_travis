import numpy as np
import pandas as pd
import requests, csv, unittest,warnings, os
from requester import url_to_csv, get_url, url_to_df,batch_url_to_csv


class TestNumComponentsReturned(unittest.TestCase):


    def test_good_url(self):
        # 1
        response = get_url('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data')
        self.assertEqual(response, None)

    def test_bad_url(self):
        # 2
        with self.assertRaises(ValueError):
            url_to_csv('https://archive.ics.uci.edu/ml/machine-bearning-databases/car/')

    def test_url_to_csv_fails_csv_parse(self):
        # Nikhil rec
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/balloons'
        # url='http://www.yahoo.com'
        with self.assertRaises(TypeError):#, msg="URL cannot be parsed as CSV"):
            url_to_csv(url)

    def test_batch_raises_runtimewarning(self):
        # 3
        urls = ['https://archive.ics.uci.edu/ml/machine-learning-databasez/car/car.data',
                'https://archive.ics.uci.edu/ml/machine-learning-databases/balloons/yellow-small.data']
        names = ['cars', 'balloons']
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            batch_url_to_csv(urls, names)
            assert len(w) == 1
            assert issubclass(w[-1].category, RuntimeWarning)
            assert "URL was skipped, not a valid url." in str(w[-1].message)
        for name in names:
            if os.path.exists(name):
                os.remove(name)


    def test_batch_same_number_csv_as_valid_url(self):
        # 4
        urls = ['https://archive.ics.uci.edu/ml/machine-learning-databasez/car/car.data',
                'https://archive.ics.uci.edu/ml/machine-learning-databases/balloons/yellow-small.data']
        names = ['cars', 'balloons']
        self.assertEquals(batch_url_to_csv(urls, names)[0], os.path.join(os.path.dirname(__file__), 'balloons.csv'))
        for name in names:
            if os.path.exists(name):
                os.remove(name)

    def test_batch_csv_contents_unique(self):
        #5
        urls = ['https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data',
                'https://archive.ics.uci.edu/ml/machine-learning-databases/balloons/yellow-small.data']
        names = ['cars', 'balloons']
        batches = batch_url_to_csv(urls,names)
        df1 = pd.read_csv(batches[0])
        df2= pd.read_csv(batches[1])
        self.assertNotEqual(df1.equals(df2), True)
        for name in names:
            if os.path.exists(name):
                os.remove(name)

    def test_batch_returns_only_valid_csvs(self):
        #6
        urls = ['https://archive.ics.uci.edu/ml/machine-learning-databasez/car/car.data',
                'https://archive.ics.uci.edu/ml/machine-learning-databases/balloons/yellow-small.data']
        names = ['cars', 'balloons']
        self.assertEquals(batch_url_to_csv(urls, names)[0],
                          os.path.join(os.path.dirname(__file__), 'balloons.csv'))


    def test_batch_returns_only_valid_csvs_again(self):
        #6
        urls = ['https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data',
                'https://archive.ics.uci.edu/ml/machine-learning-databasez/balloons/yellow-small.data']
        names = ['cars', 'balloons']
        self.assertEquals(batch_url_to_csv(urls, names)[0], os.path.join(os.path.dirname(__file__), 'cars.csv'))

    def test_batch_returns_correct_num_files_bad_url(self):
        # 7
        urls = ['https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data',
                'https://archive.ics.uci.edu/ml/machine-learning-databasez/balloons/yellow-small.data']
        names = ['cars', 'balloons']
        self.assertEquals(len(batch_url_to_csv(urls, names)), 1)

    def test_batch_returns_correct_num_files_good_urls(self):
        # 7
        urls = ['https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data',
                'https://archive.ics.uci.edu/ml/machine-learning-databases/balloons/yellow-small.data']
        names = ['cars', 'balloons']
        self.assertEquals(len(batch_url_to_csv(urls, names)), 2)


    def test_batch_assertion_error(self):
        # 8
        urls = ['https://archive.ics.uci.edu/ml/machine-learning-databases/balloons',
                'https://archive.ics.uci.edu/ml/machine-learning-databases/balloons']
        names = ['balloons_1', 'balloons_2']
        with self.assertRaises(AssertionError):
            batch_url_to_csv(urls,names)


    def test_url_to_df_datframe_object(self):
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data'
        frame = url_to_df(url)
        self.assertTrue(type(frame), pd.DataFrame())


    def test_url_to_df_DataFrame_rows(self):
        # 10
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data'
        df_rows = url_to_df(url).shape[0]
        with requests.Session() as s:
            download = s.get(url)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            csv_rows = len(my_list)
        self.assertEqual(df_rows, csv_rows)



if __name__ == '__main__':
    unittest.main(verbosity=20)