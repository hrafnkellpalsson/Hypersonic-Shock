"""
Constants needed for project 6.
All constants are in standard SI units, except for the altitude list.
"""

# 3rd party imports
import numpy

# Value obtained from http://en.wikipedia.org/wiki/Gas_constant
R = 287.058

# On page 2 of the 1987 Srinivasan report it says that the reference conditions they use 
# are at 1 atm and 273.15K. XZ says we can use the perfect gas relation to compute other
# reference conditions. Value of atmospheric pressure in Pa is obtained from
# http://en.wikipedia.org/wiki/Atmospheric_pressure.
p0 = 101325
T0 = 273.15
rho0 = p0 / (R * T0)

# When we can treat the air as perfect in the project, and only then, the values of the
# specific heats are useful. Turns out they are only used for unit testing.
# Value for c_p is obtained from http://en.wikipedia.org/wiki/Specific_heat
c_p = 1003.5
# Value for gamma is obtained from http://en.wikipedia.org/wiki/Heat_capacity_ratio
gamma = 1.403
c_v = c_p / gamma

# Converstion from feet to meters.
feet_to_m = 0.3048

# The altitude, in feet, on figures 14.4 and 14.5 page 609 and 610 in Anderson.
altitude = ['35.900', '59.800', '82.200', '100.000', '120.300',
            '154.800', '173.500', '200.100', '230.400', '259.700',
            '294.800', '322.900']

# Upstream values of pressure corresponding to the altitude.
# Values are obtained from tables in 1963 Nasa technical report by Huber (ref. [165] Anderson)
p1_upstream = numpy.array([0.225, 0.7135E-1, 0.2438E-1, 0.1067E-1, 0.4462E-2,
                           0.1161E-2, 0.5826E-3, 2.052E-4, 5.042E-5, 9.631E-6,
                           1.064E-6, 2.119E-7]) * p0

# Upstream values of temperature corresponding to the altitude.
# Values are obtained from tables in 1963 Nasa technical report by Huber (ref. [165] Anderson)
T1_upstream = numpy.array([217., 217., 217., 233., 252.,
                           283., 283., 247., 205., 166.,
                           166., 199.])
