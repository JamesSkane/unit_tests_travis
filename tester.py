import unittest
import numpy as np
from requester import add, url_to_csv, get_url
from numpy.testing import assert_array_almost_equal
import requests
from urlparse import urlparse





class TestNumComponentsReturned(unittest.TestCase):

    def test_url(self):
        response = get_url('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data')
        self.assertEqual(response, 200)

    def test_bad_url(self):
        with self.assertRaises(TypeError):
            url_to_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/')


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