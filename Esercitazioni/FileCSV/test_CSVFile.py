import unittest
from CSVFile import NumericalCSVFile

#Testing
class TestGetData(unittest.TestCase):

    def test_get_data_first_element(self):
        x = NumericalCSVFile('shampoo_sales.csv')
        print('{}'.format(x.get_data(0,0)))
        #self.assertEqual(x.get_data(0,0), ['01-01-2012', 266.0])