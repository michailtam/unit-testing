'''
This code snippet shows how command line arguments can be passed via the terminal using Python,
the argparse library and executing unit testing. The code executes three simple tests:

1. Checks if the command line image name is the right one
2. Checks if the training-set len is the right one
2. Checks if the test-set len is the right one

NOTE: For simplicity, the Dataset class holds only the len of the training and test
set and is set fixed. These values are getting calculated in real applications
based on the dataset data. The code sipped only shows the methodology.

To execute the test (without any error) issue the following command in the terminal:
    python test_unit.py --image images/img_0004.png --train-len 10000 --test-len 1000
Changing the above values leads to the respective error.

Output:
...
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
'''

import argparse
import unittest

""" Dataset class """
class Dataset():

    def __init__(self):
        self.__train_len = 10000
        self.__test_len = 1000

    @property
    def get_train_len(self):
        return self.__train_len

    @property
    def get_test_len(self):
        return self.__test_len


""" Unit testing class """
class UnitTesting(unittest.TestCase):

    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-i", "--image", required=True, help="Path to the image")
        self.parser.add_argument("-d", "--train-len", required=True, help="Path to the training set")
        self.parser.add_argument("-t", "--test-len", required=True, help="Path to the test set")
        self.__dataset = Dataset()

    def test_parsing_cmd_args(self):
        """ Tests whether the command line argument of the image name is the right one. """
        self.__args = vars(self.parser.parse_args())
        self.assertEqual(str(self.__args["image"]), "images/img_0004.png")

    def test_len_trainset(self):
        """ Tests if the len of the training set is the desired. """
        self.assertEqual(self.__dataset.get_train_len, 10000)

    def test_len_testset(self):
        """ Tests if the len of the test set is the desired. """
        self.assertEqual(self.__dataset.get_test_len, 1000)

if __name__ == "__main__":
    unittest.main(__name__, argv=['main'], exit=False)