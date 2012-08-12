"""
The coefficients for the Srinivasan-Tannehill-Weilmuenster correlations, p(e, rho) and T(p, rho), are written out.
A methods to extract the correct coefficients based on the values of Y and Z.
"""

# 3rd party imports
import numpy

def load_pressure_coefficients(Y, Z):
    """
    Load the correct set of coefficients for the Srinivasan-Tannehill-Weilmuenster p(e, rho) correlation,
    for given values of Y and Z.
    
    :param Y: Y paramater in the p(e, rho) correlation.
    :param Z: Z paramater in the p(e, rho) correlation.

    :return coefficients: The correct set of coefficients.

    Note: The naming convention for the coefficient vectors is as folllows:
        The first "subscript" refers to the table number and the second "subscript" refers to the Z column
        in that table.
    """
    # Table A.1
    if -7.0 <= Y <= -4.5:
        if Z <= 0.65:
            sign = 1.
            coefficients = A11
        elif 0.65 < Z <= 1.50:
            sign = -1.
            coefficients = A12
        elif 1.50 < Z <= 2.20:
            sign = 1.
            coefficients = A13
        elif 2.20 < Z <= 3.05:
            sign = 1.
            coefficients = A14
        elif 3.05 < Z <= 3.40:
            sign = 1.
            coefficients = A15
        elif 3.40 < Z:
            sign = 1.
            coefficients = A16
        else:
            print "Something's wrong, we shouldn't be able to get here."
    # Table A.2     
    elif -4.5 < Y <= -0.5:
        if Z <= 0.65:
            sign = 1.
            coefficients = A21
        elif 0.65 < Z <= 1.50:
            sign = 1.
            coefficients = A22
        elif 1.50 < Z <= 2.22:
            sign = 1.
            coefficients = A23
        elif 2.22 < Z <= 2.95:
            sign = 1.
            coefficients = A24
        elif 2.95 < Z:
            sign = 1.
            coefficients = A25
        else:
            print "Something's wrong, we shouldn't be able to get here."
    # Table A.3
    elif -0.5 < Y <= 3.0:
        if Z <= 0.65:
            sign = 1.
            coefficients = A31
        elif 0.65 < Z <= 1.70:
            sign = 1.
            coefficients = A32
        elif 1.70 < Z <= 2.35:
            sign = 1.
            coefficients = A33
        elif 2.35 < Z:
            sign = 1.
            coefficients = A34
        else:
            print "Something's wrong, we shouldn't be able to get here."

    else:
        print 'The value of Y, and therefore rho, is out allowable range'

    out_dict = {'coefficients': coefficients,
                'sign': sign}
    return out_dict

def load_temperature_coefficients(Y, Z):
    """
    Load the correct set of coefficients for the Srinivasan-Tannehill-Weilmuenster T(p, rho) correlation,
    for given values of Y and Z.
    
    :param Y: Y paramater in the T(p, rho) correlation.
    :param Z: Z paramater in the T(p, rho) correlation.

    :return coefficients: The correct set of coefficients.

    Note: The naming convention for the coefficient vectors is as folllows:
        The first "subscript" refers to the table number and the second "subscript" refers to the Z column
        in that table.
    """
    # Table A.10
    if -7.0 <= Y <= -4.5:
        if 0.25 < Z <= 0.95:
            sign = 1.
            coefficients = A101
        elif 0.95 < Z <= 1.40:
            sign = 1.
            coefficients = A102
        elif 1.40 < Z <= 1.95:
            sign = 1.
            coefficients = A103
        elif 1.95 < Z:
            sign = 1.
            coefficients = A104
        else:
            print "Something's wrong, we shouldn't be able to get here."
    # Table A.11    
    elif -4.5 < Y <= -0.5:
        if 0.25 < Z <= 0.95:
            sign = 1.
            coefficients = A111
        elif 0.95 < Z <= 1.45:
            sign = 1.
            coefficients = A112
        elif 1.45 < Z <= 2.05:
            sign = 1.
            coefficients = A113
        elif 2.05 < Z:
            sign = 1.
            coefficients = A114
        else:
            print "Something's wrong, we shouldn't be able to get here."
    # Table A.12
    elif -0.5 < Y <= 3.0:
        if 0.25 < Z <= 1.00:
            sign = 1.
            coefficients = A121
        elif 1.00 < Z <= 1.45:
            sign = 1.
            coefficients = A122
        elif 1.45 < Z:
            sign = 1.
            coefficients = A123
        else:
            print "Something's wrong, we shouldn't be able to get here."

    else:
        print 'The value of Y, and therefore rho, is out allowable range'

    out_dict = {'coefficients': coefficients,
                'sign': sign}
    return out_dict

A11 = numpy.array([1.3965,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.])

A12 = numpy.array([1.52792,
                   -1.26953E-2,
                   -6.13514E-1,
                   -5.08262E-2,
                   -5.49384E-3,
                   6.31835E-1,
                   4.75120E-5,
                   3.34012E-2,
                   -3.18468E-4,
                   -2.19921E-1,
                   -4.96286E1,
                   -1.17932E1,
                   6.91028E1,
                   4.40405E1,
                   5.09249,
                   1.37308E1,
                   -1.40326,
                   -1.78726E1,
                   2.08988E-1,
                   -1.86943E1,
                   24.60452,
                   -2.0,
                   -2.093022E1,
                   0.])

A13 = numpy.array([-1.70333E1,
                    -5.08545E-1,
                    2.46299E1,
                    4.45617E-1,
                    -8.95298E-3,
                    -1.10204E1,
                    2.29618E-3,
                    -9.89727E-2,
                    -2.89186E-4,
                    1.62903,
                    1.86797E1,
                    5.19662E-1,
                    -2.41338E1,
                    -4.34837E-1,
                    9.16089E-3,
                    1.02035E1,
                    -1.52082E-3,
                    9.70762E-2,
                    3.46482E-4,
                    -1.3946,
                    -1.42762E2,
                    -1.647088,
                    7.660312E1,
                    8.259346E-1])

A14 = numpy.array([2.24374,
                   1.03073E-1,
                   -5.32238E-1,
                   -5.59852E-2,
                   3.56484E-3,
                   -4.80156E-2,
                   -1.01359E-4,
                   1.06794E-2,
                   1.59127E-4,
                   3.66035E-2,
                   -5.70378,
                   -3.10056E-1,
                   5.01094,
                   1.80411E-1,
                   -9.49361E-3,
                   -1.40331,
                   1.94839E-3,
                   -2.79718E-2,
                   -2.24908E-4,
                   1.20278E-1,
                   1.139755E2,
                   -4.985467,
                   -4.223833E1,
                   2.009706])

A15 = numpy.array([-0.20807E2,
                    0.40197,
                    0.22591E2,
                    -0.25660,
                    -0.95833E-3,
                    -0.77174E1,
                    0.23966E-2,
                    0.4606E-1,
                    0.33671E-3,
                    0.878,
                    -0.21737E3,
                    -0.46927E1,
                    0.18101E3,
                    0.26621E1,
                    -0.34759E-1,
                    -0.50019E2,
                    0.64681E-2,
                    -0.38381,
                    -0.70391E-3,
                    0.45795E1,
                    0.4544373E3,
                    0.1250133E2,
                    -0.1376001E3,
                    -0.3641774E1])

A16 = numpy.array([-5.22951E1,
                    -4.00011E-1,
                    4.56439E1,
                    2.24484E-1,
                    -3.73775E-3,
                    -1.29756E1,
                    2.43161E-3,
                    -2.79517E-2,
                    2.24755E-4,
                    1.22998,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.])

A21 = numpy.array([1.398,                                  
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.])

A22 = numpy.array([1.39123,
                   -4.08321E-3,
                   1.42545E-2,
                   1.41769E-2,
                   2.57225E-4,
                   6.2555E-2,
                   6.52912E-4,
                   -7.83637E-3,
                   8.46912E-5,
                   -9.78720E-2,
                   5.80955,
                   -1.82302E-1,
                   -9.62396,
                   1.79619E-1,
                   -2.30518E-2,
                   5.27047,
                   1.1872E-2,
                   -3.65507E-2,
                   -3.35499E-4,
                   -9.19897E-1,
                   14.2,
                   0.,
                   -1.00E1,
                   0.])

A23 = numpy.array([-1.20784,
                    -2.57909E-1,
                    5.02307,
                    2.87201E-1,
                    -9.95577E-3,
                    -3.20619,
                    5.23524E-3,
                    -7.50405E-2,
                    -1.45574E-4,
                    6.51564E-1,
                    -6.62841,
                    2.77112E-2,
                    7.30762,
                    -7.6823E-2,
                    7.19421E-3,
                    -2.33161,
                    -3.62463E-3,
                    3.04767E-2,
                    1.62777E-4,
                    1.66856E-1,
                    1.255324E2,
                    2.015335,
                    -6.390747E1,
                    -6.515225E-1])

A24 = numpy.array([-2.26460,
                    -7.82263E-2,
                    4.90497,
                    7.18096E-2,
                    -3.06443E-3,
                    -2.24750,
                    1.74209E-3,
                    -1.31641E-2,
                    2.84214E-5,
                    3.33658E-1,
                    -1.47904E1,
                    -1.76627E-1,
                    1.35036E1,
                    8.77280E-2,
                    -2.13327E-3,
                    -3.95372,
                    7.15487E-4,
                    -8.96151E-3,
                    7.30928E-5,
                    3.63229E-1,
                    1.788542E2,
                    6.317894,
                    -6.756741E1,
                    -2.46006])

A25 = numpy.array([-1.66904E1,
                    -2.58318E-1,
                    1.78350E1,
                    1.54898E-1,
                    -9.71263E-3,
                    -5.94108,
                    3.97740E-3,
                    -2.01335E-2,
                    9.04300E-5,
                    6.60432E-1,
                    8.54690E1,
                    1.17554E1,
                    -7.21760E1,
                    -7.15723,
                    -4.16150E-2,
                    2.01758E1,
                    1.38147E-2,
                    1.08990,
                    5.45184E-4,
                    -1.86438,
                    2.883262E2,
                    1.248536E1,
                    -8.816985E1,
                    -3.720309])

A31 = numpy.array([1.3988,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.])

A32 = numpy.array([1.37062,
                   1.29673E-2,
                   1.11418E-1,
                   -3.26912E-2,
                   1.06869E-3,
                   -1.06133E-1,
                   -2.00286E-3,
                   1.90251E-2,
                   2.38305E-4,
                   3.02210E-3,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.,
                   0.])

A33 = numpy.array([3.43846E-2,
                   -2.33584E-1,
                   2.85574,
                   2.59787E-1,
                   -10.89927E-3,
                   -1.94785,
                   4.23659E-3,
                   -6.73865E-2,
                   3.85712E-4,
                   4.08518E-1,
                   -4.20569,
                   1.33139E-1,
                   4.51236,
                   -1.66341E-1,
                   1.67787E-3,
                   -1.35516,
                   -1.10022E-3,
                   4.91716E-2,
                   3.06676E-4,
                   7.52509E-2,
                   1.757042E2,
                   -2.163278,
                   -8.833702E1,
                   1.897543])

A34 = numpy.array([-1.70633,
                    -1.48403E-1,
                    4.23104,
                    1.37290E-1,
                    -9.10934E-3,
                    -1.97292,
                    3.85707E-3,
                    -2.81830E-2,
                    2.69026E-4,
                    2.95882E-1,
                    3.41580E1,
                    -1.89972E1,
                    -4.0858E1,
                    1.30321E1,
                    -8.01272E-1,
                    1.60826E1,
                    2.75121E-1,
                    -2.23386,
                    -1.77969E-4,
                    -2.08853,
                    2.561323E2,
                    1.737089E2,
                    -9.05889E1,
                    -5.838803E1])

A101 = numpy.array([1.23718E-1,
                    1.08623E-2,
                    2.24239E-1,
                    -8.24608E-2,
                    -1.17615E-3,
                    1.18397,
                    -1.87566E-3,
                    6.4852E-2,
                    -1.19155E-4,
                    -5.52634E-1,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.])

A102 = numpy.array([-8.12952,
                     -8.28637E-1,
                     2.26904E1,
                     1.41132,
                     -2.98633E-2,
                     -1.91806E1,
                     2.70066E-2,
                     -5.78875E-1,
                     -2.28103E-4,
                     5.62580,
                     -3.99845,
                     2.26369E-1,
                     2.52870,
                     -7.28448E-1,
                     1.09769E-2,
                     2.99238,
                     -1.83819E-2,
                     3.91440E-1,
                     -1.51380E-4,
                     -2.04463,
                     -3.887015E1,
                     -2.908228E1,
                     4.070557E1,
                     2.682347E1])

A103 = numpy.array([-1.98573E1,
                     -1.67225,
                     3.76159E1,
                     2.10964,
                     -3.40174E-2,
                     -2.22215E1,
                     2.31712E-2,
                     -6.44596E-1,
                     -9.80275E-5,
                     4.40486,
                     -5.36809,
                     2.41201E-1,
                     -1.25881,
                     -8.62744E-1,
                     -3.79774E-3,
                     5.58609,
                     -7.81335E-3,
                     3.78963E-1,
                     -3.80005E-4,
                     -1.81566,
                     2.08E1,
                     -2.56E1,
                     1.0,
                     1.80E1])

A104 = numpy.array([-2.33271E1,
                     -1.89958,
                     3.21440E1,
                     1.68622,
                     -4.42123E-2,
                     -1.38645E1,
                     2.82629E-2,
                     -3.40976E-1,
                     6.63272E-4,
                     2.04466,
                     8.35474,
                     1.71347,
                     -1.60715E1,
                     -1.63139,
                     4.14641E-2,
                     8.70275,
                     -2.30068E-2,
                     3.60966E-1,
                     1.53246E-5,
                     -1.46166,
                     1.115884E2,
                     -6.452606,
                     -5.337863E1,
                     2.026986])

A111 = numpy.array([2.03910E-2,
                    7.67310E-3,
                    8.48581E-1,
                    -2.93086E-2,
                    8.40269E-4,
                    2.67251E-1,
                    -1.47701E-3,
                    2.37262E-2,
                    3.13687E-5,
                    -1.41973E-1,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.])

A112 = numpy.array([-5.12404,
                     -2.8474E-1,
                     1.54532E1,
                     4.52475E-1,
                     -1.22881E-2,
                     -1.35181E1,
                     8.56845E-3,
                     -1.68725E-1,
                     -3.25256E-4,
                     4.18451,
                     7.52564,
                     8.35238E-1,
                     -1.95558E1,
                     -1.23393,
                     3.34510E-2,
                     1.71779E1,
                     -2.34269E-2,
                     4.54628E-1,
                     4.81788E-4,
                     -5.09936,
                     6.148442E1,
                     -1.828123E1,
                     -5.468755E1,
                     1.562500E1])

A113 = numpy.array([-1.23779E1,
                     -1.14728,
                     2.41382E1,
                     1.38957,
                     -3.63693E-2,
                     -1.42844E1,
                     2.24265E-2,
                     -4.06553E-1,
                     -3.23888E-4,
                     2.8762,
                     4.40782,
                     1.33046,
                     -1.15405E1,
                     -1.59892,
                     5.30580E-2,
                     8.57309,
                     -3.10376E-2,
                     4.71274E-1,
                     4.77650E-4,
                     -1.96233,
                     1.4075E2,
                     -6.499992,
                     -7.75E1,
                     5.0])

A114 = numpy.array([-1.27244E1,
                     -1.66684,
                     1.72708E1,
                     1.45307,
                     -3.64515E-2,
                     -6.97208,
                     1.90463E-2,
                     -3.04323E-1,
                     4.80787E-4,
                     9.67524E-1,
                     7.71330,
                     5.0834E-1,
                     -9.8211,
                     -4.49138E-1,
                     -9.41787E-4,
                     4.16530,
                     -2.40293E-3,
                     9.63923E-2,
                     -8.28450E-4,
                     -5.88807E-1,
                     -1.092654E3,
                     -3.05312E2,
                     4.656243E2,
                     1.312498E2])

A121 = numpy.array([-1.54141E-3,
                     6.58337E-4,
                     9.82201E-1,
                     -3.85028E-3,
                     1.23111E-4,
                     3.77441E-2,
                     -4.08210E-4,
                     4.56963E-3,
                     2.13592E-5,
                     -2.35172E-2,
                     0.,
                     0.,
                     0.,
                     0.,
                     0.,
                     0.,
                     0.,
                     0.,
                     0.,
                     0.,
                     0.,
                     0.,
                     0.,
                     0.])

A122 = numpy.array([8.06492E-1,
                    9.91293E-2,
                    -1.70742,
                    -2.28264E-1,
                    5.03500E-3,
                    3.02351,
                    -6.13927E-3,
                    1.31574E-1,
                    1.69824E-4,
                    -1.12755,
                    -1.17930E-1,
                    -2.12207E-1,
                    1.36524,
                    4.05886E-1,
                    -1.88260E-2,
                    -2.10926,
                    1.65486E-2,
                    -1.89881E-1,
                    -5.1140E-4,
                    8.79806E-1,
                    1.959604E2,
                    -4.269391E1,
                    -1.734931E2,
                    3.762898E1])

A123 = numpy.array([-1.66249,
                     -8.91113E-2,
                     4.11648,
                     8.78093E-2,
                     -3.09742E-3,
                     -1.84445,
                     1.99879E-3,
                     -7.50324E-3,
                     6.85472E-5,
                     3.05784E-1,
                     1.11555E1,
                     1.3210,
                     -1.71236E1,
                     -1.2919,
                     6.28124E-2,
                     8.63804,
                     -3.07949E-2,
                     3.07809E-1,
                     1.57743E-3,
                     -1.42634,
                     1.330611E2,
                     8.979635,
                     -7.265298E1,
                     -2.449009])

