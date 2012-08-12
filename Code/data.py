"""
Arrays of upstream velocity where one line in the array corresponds to the velocity range
for a single curve.

A function for reading csv files outputted by Engauge. This function is then applied to all
the engauge csv files and the resulting data is stored.
"""

# Python library imports
import os
# 3rd party imports
import numpy

def read_engauge_csv(file):
    """
    Read the values from a csv file by Engauge with n lines into a (n-1) by 2 numpy.array.
    n-1 because we skip the header.

    :param file: Full path to a csv file outputted by Engauge.

    :return engauge_values: An (n-1) by 2 numpy.array with numerical value from the Engauge
    csv file.
    """

    file = open(file)
    lines = file.readlines()
    number_of_lines = len(lines)
    number_of_entries = number_of_lines - 1
    engauge_values = numpy.empty([number_of_entries, 2])

    for i, line in enumerate(lines[1:]):
        xyvalues = line.split(',')

        xvalue = xyvalues[0]
        xvalue = xvalue.rstrip('\n')
        xvalue = float(xvalue)
        engauge_values[i,0] = xvalue

        yvalue = xyvalues[1]
        xvalue = yvalue.rstrip('\n')
        yvalue = float(yvalue)
        engauge_values[i,1] = yvalue

    return engauge_values

def read_multiple_engauge_csv(dir, filenames):
    """
    Read values from multiple Engauge csv files into a list.

    :param dir: The directory of the Engauge csv files.
    :param filenames: A list of filenames of Engauge csv files, including the .csv ending.
    """

    engauge_list = []
    for filename in filenames:
        engauge_values = read_engauge_csv(os.path.join(dir, filename))
        engauge_list.append(engauge_values)
    
    return engauge_list

def read_single_engauge_csv(file):
    """
    Read the values from a csv file by Engauge with n lines into a (n-1) by 2 numpy.array.
    n-1 because we skip the header.

    :param file: Full path to a csv file outputted by Engauge.

    :return engauge_values: An (n-1) by 2 numpy.array with numerical value from the Engauge
    csv file.
    """

    file = open(file)
    lines = file.readlines()
    number_of_lines = len(lines)
    number_of_entries = number_of_lines - 1
    number_of_columns = 13
    engauge_values = numpy.empty([number_of_entries, number_of_columns])

    for i, line in enumerate(lines[1:]):
        values = line.split(',')

        xvalue = values[0]
        xvalue = xvalue.rstrip('\n')
        xvalue = float(xvalue)
        engauge_values[i,0] = xvalue

        for j in range(number_of_columns-1):
            data_index = j + 1
            if data_index > 12:
                print 'jasveimertha'
            data_value = values[data_index]
            data_value = data_value.rstrip('\n')
            data_value = float(data_value)
            engauge_values[i,data_index] = data_value

    return engauge_values


engauge_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','engauge_csv'))

csv_filenames_144a = ['144a_35900.csv', '144a_154800.csv', '144a_322900.csv']
engauge_list_144a = read_multiple_engauge_csv(engauge_dir, csv_filenames_144a)

csv_filenames_144b = ['144b_35900.csv', '144b_154800.csv', '144b_322900.csv']
engauge_list_144b = read_multiple_engauge_csv(engauge_dir, csv_filenames_144b)

csv_filenames_145a = ['145a_35900.csv', '145a_154800.csv', '145a_322900.csv']
engauge_list_145a = read_multiple_engauge_csv(engauge_dir, csv_filenames_145a)

csv_filenames_145b = ['145b_35900.csv', '145b_154800.csv', '145b_322900.csv']
engauge_list_145b = read_multiple_engauge_csv(engauge_dir, csv_filenames_145b)


step_size = 0.2
u1_vector_feet_35900 = numpy.arange(3.5, 18.3 + step_size/2., step_size) * 1E3
u1_vector_feet_59800 = numpy.arange(3.5, 19.4 + step_size/2., step_size) * 1E3
u1_vector_feet_82200 = numpy.arange(3.5, 20.8 + step_size/2., step_size) * 1E3
u1_vector_feet_100000 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_120300 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_154800 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_173500 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_200100 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_230400 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_259700 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_294800 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_322900 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_144a_feet = [u1_vector_feet_35900,
                u1_vector_feet_59800,
                u1_vector_feet_82200,
                u1_vector_feet_100000,
                u1_vector_feet_120300,
                u1_vector_feet_154800,
                u1_vector_feet_173500,
                u1_vector_feet_200100,
                u1_vector_feet_230400,
                u1_vector_feet_259700,
                u1_vector_feet_294800,
                u1_vector_feet_322900]


step_size = 0.2
u1_vector_feet_35900 = numpy.arange(16., 28.2 + step_size/2., step_size) * 1E3
u1_vector_feet_59800 = numpy.arange(16., 30. + step_size/2., step_size) * 1E3
u1_vector_feet_82200 = numpy.arange(16., 32.7 + step_size/2., step_size) * 1E3
u1_vector_feet_100000 = numpy.arange(16., 35. + step_size/2., step_size) * 1E3
u1_vector_feet_120300 = numpy.arange(16., 37.9 + step_size/2., step_size) * 1E3
u1_vector_feet_154800 = numpy.arange(16., 41.3 + step_size/2., step_size) * 1E3
u1_vector_feet_173500 = numpy.arange(16., 43.3 + step_size/2., step_size) * 1E3
u1_vector_feet_200100 = numpy.arange(16., 46. + step_size/2., step_size) * 1E3
u1_vector_feet_230400 = numpy.arange(16., 46. + step_size/2., step_size) * 1E3
u1_vector_feet_259700 = numpy.arange(16., 46. + step_size/2., step_size) * 1E3
u1_vector_feet_294800 = numpy.arange(16., 46. + step_size/2., step_size) * 1E3
u1_vector_feet_322900 = numpy.arange(16., 46. + step_size/2., step_size) * 1E3
u1_144b_feet = [u1_vector_feet_35900,
                u1_vector_feet_59800,
                u1_vector_feet_82200,
                u1_vector_feet_100000,
                u1_vector_feet_120300,
                u1_vector_feet_154800,
                u1_vector_feet_173500,
                u1_vector_feet_200100,
                u1_vector_feet_230400,
                u1_vector_feet_259700,
                u1_vector_feet_294800,
                u1_vector_feet_322900]


step_size = 0.2
u1_vector_feet_35900 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_59800 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_82200 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_100000 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_120300 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_154800 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_173500 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_200100 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_230400 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_259700 = numpy.arange(3.5, 22. + step_size/2., step_size) * 1E3
u1_vector_feet_294800 = numpy.arange(3.5, 20.9 + step_size/2., step_size) * 1E3
u1_vector_feet_322900 = numpy.arange(3.5, 19.6 + step_size/2., step_size) * 1E3
u1_145a_feet = [u1_vector_feet_35900,
                u1_vector_feet_59800,
                u1_vector_feet_82200,
                u1_vector_feet_100000,
                u1_vector_feet_120300,
                u1_vector_feet_154800,
                u1_vector_feet_173500,
                u1_vector_feet_200100,
                u1_vector_feet_230400,
                u1_vector_feet_259700,
                u1_vector_feet_294800,
                u1_vector_feet_322900]


step_size = 0.2
u1_vector_feet_35900 = numpy.arange(16., 28.5 + step_size/2., step_size) * 1E3
u1_vector_feet_59800 = numpy.arange(16., 30.5 + step_size/2., step_size) * 1E3
u1_vector_feet_82200 = numpy.arange(16., 33. + step_size/2., step_size) * 1E3
u1_vector_feet_100000 = numpy.arange(16., 35.5 + step_size/2., step_size) * 1E3
u1_vector_feet_120300 = numpy.arange(16., 38.5 + step_size/2., step_size) * 1E3
u1_vector_feet_154800 = numpy.arange(16., 42. + step_size/2., step_size) * 1E3
u1_vector_feet_173500 = numpy.arange(16., 44.5 + step_size/2., step_size) * 1E3
u1_vector_feet_200100 = numpy.arange(16., 46. + step_size/2., step_size) * 1E3
u1_vector_feet_230400 = numpy.arange(16., 46. + step_size/2., step_size) * 1E3
u1_vector_feet_259700 = numpy.arange(16., 46. + step_size/2., step_size) * 1E3
u1_vector_feet_294800 = numpy.arange(16., 46. + step_size/2., step_size) * 1E3
u1_vector_feet_322900 = numpy.arange(16., 46. + step_size/2., step_size) * 1E3
u1_145b_feet = [u1_vector_feet_35900,
                u1_vector_feet_59800,
                u1_vector_feet_82200,
                u1_vector_feet_100000,
                u1_vector_feet_120300,
                u1_vector_feet_154800,
                u1_vector_feet_173500,
                u1_vector_feet_200100,
                u1_vector_feet_230400,
                u1_vector_feet_259700,
                u1_vector_feet_294800,
                u1_vector_feet_322900]
