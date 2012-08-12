"""
Test functions in calculators.py module.
"""

# Python library
import unittest
import os
# 3rd party imports
import numpy

# The module/functions to test
import data

class TestCase_calculators(unittest.TestCase):
    """
    Tests class for functions in data.py
    """

    def no_test_read_engauge_csv(self):
        """
        Test data.read_engauage_csv()
        """
        engauge_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','engauge_csv'))
        filename = '144a_35900.csv'        
        engauge_values_known = numpy.array([[3374.54,812.964],
                                            [4747.6,1339.38],
                                            [5914.66,1885.6],
                                            [6928.66,2413.78],
                                            [7939.92,2988.95],
                                            [8871.57,3484.66],
                                            [9808.3,3942.76],
                                            [11127.1,4603.33],
                                            [12372.6,5306.53],
                                            [13304.2,5893.84],
                                            [14120.1,6430.05],
                                            [14615.1,6730.61],
                                            [15275.5,7093.77],
                                            [15759.7,7326.26],
                                            [16121.7,7495.94]])
        file = os.path.join(engauge_dir, filename)
        engauge_values_read = data.read_engauge_csv(file)
        
        self.assertTrue(engauge_values_known.shape == engauge_values_read.shape)

        dimensions = engauge_values_read.shape
        for i,j in zip(range(dimensions[0]), range(dimensions[1])):
            self.assertTrue(engauge_values_known[i,j] == engauge_values_read[i,j])
                       
    def no_test_read_multiple_engauge_csv(self):
        """
        Test data.read_multiple_engauge_csv()
        """
        engauge_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','engauge_csv'))
        filenames = ['144a_35900.csv', '144a_59800.csv']
        engauge_list = data.read_multiple_engauge_csv(engauge_dir, filenames)
        print 'Ouptut from test_read_multiple_engauge_csv() in data_unittest.py:'
        print engauge_list

    def test_read_single_engauge_csv(self):
        """
        Test data.read_single_engauge_csv()
        """
        engauge_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','engauge_csv'))
        filename = '144b_200100_to_294800.csv'
        file = os.path.join(engauge_dir, filename)
        engauge_array_144b = data.read_single_engauge_csv(file)
        print  'shape:', engauge_array_144b.shape
        # print engauge_array
    





if __name__ == '__main__':
    unittest.main()
