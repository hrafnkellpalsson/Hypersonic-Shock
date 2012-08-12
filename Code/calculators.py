"""
Functions to calculate thermodynamics properties of real gas across a normal shock wave.
Inviscied, equilibrium flow is assumed.
Also functions to calculate equillibrium thermodynamic properties of air when considered
a real gas mixture.
"""

# Library imports
import sys
# 3rd party imports
import numpy
import scipy
from scipy import optimize
# Local imports
import correlation_coefficients
import constants

def p2_shock_wave(p1, rho1, u1, rho1_to_rho2):
    """
    Calculate the pressure of a real gas mixture behind a normal shock wave in inviscid equilibrium flow.

    :param p1: The pressure of the gas before the shock.
    :param rho1: The density of the gas before the shock.
    :param u1: The velocity of the gas before the shock.
    :param rho1_to_rho2: The ratio of gas density across the shock, more specifically rho1/rho2.

    :return p2: The pressure behind the shock.
    """

    p2 = p1 + rho1 * numpy.power(u1, 2.) * (1 - rho1_to_rho2)
    return p2

def h2_shock_wave(h1, u1, rho1_to_rho2):
    """
    Calculate the static enthalpy of a real gas mixture behind a normal shock wave in inviscid equilibrium flow.

    :param h1: The static enthalpy of the gas before the shock.
    :param u1: The velocity of the gas before the shock.
    :param rho1_to_rho2: The ratio of gas density across the shock, more specifically rho1/rho2.

    :return h2: The static enthalpy behind the shock.
    """

    h2 = h1 + (numpy.power(u1, 2.) / 2) * (1 - numpy.power(rho1_to_rho2, 2.))
    return h2

def get_gamma_helper(coefficients10, Y, Z):
    """
    Helper function for get_gamma()
    """

    c1 = coefficients10[0]
    c2 = coefficients10[1]
    c3 = coefficients10[2]
    c4 = coefficients10[3]
    c5 = coefficients10[4]
    c6 = coefficients10[5]
    c7 = coefficients10[6]
    c8 = coefficients10[7]
    c9 = coefficients10[8]
    c10 = coefficients10[9]

    terms1to5 = c1 + c2*Y + c3*Z + c4*Y*Z + c5*numpy.power(Y,2.)
    terms6to8 = c6*numpy.power(Z,2.) + c7*numpy.power(Y,2.)*Z + c8*Y*numpy.power(Z,2.)
    terms9to10 = c9*numpy.power(Y,3.) + c10*numpy.power(Z,3.)
    terms1to10 = terms1to5 + terms6to8 + terms9to10

    return terms1to10    

def get_gamma(coefficients, Y, Z, sign):
    """
    The Srinivasan-Tannehill-Weilmuenster correlations for p(e, rho) and T(p, rho) have a 
    certain structure. Note that the sum of the "coefficient terms" (called gamma in the
    p(e, rho) correlation) are almost identical, differing at most by one sign in the 
    denominator.
    Take advantage of that structure to write only a single function involving the sum
    of the coefficient terms.

    :param coefficients: A 1D array of the 24 coefficients in numerically ascending order.
        I.e. numpy.array([c1, c2, ..., c24])
    :param Y: The Y parameter for the given correlation.
    :param Z: The Z paramter for the given correlation
    :param sign: The sign of the exponential term in the correlation.

    :return gamma: The sum of the coefficient terms.
    """

    coefficients1to10 = coefficients[0:10]
    terms1to10 = get_gamma_helper(coefficients1to10, Y, Z)
    
    coefficients11to20 = coefficients[10:20]
    terms11to20 = get_gamma_helper(coefficients11to20, Y, Z)

    c21 = coefficients[20]
    c22 = coefficients[21]
    c23 = coefficients[22]
    c24 = coefficients[23]
    terms21to24 = c21 + c22*Y + c23*Z + c24*Y*Z
    
    gamma = terms1to10 + terms11to20 / (1 + sign * numpy.exp(terms21to24))
    return gamma
    
def srinivasan_p(e, rho):
    """
    Calculate the pressure of air, when considered a real gas mixture, given the internal energy and density.

    :param e: The internal energy of the air.
    :param rho: The density of the air.

    :return p: The pressure of the air.
    """

    rho0 = constants.rho0
    T0 = constants.T0
    R = constants.R

    Y = numpy.log10(rho / rho0)
    Z = numpy.log10(e / (R * T0))
    # print 'Y, Z = ', Y, Z
   
    out_dict = correlation_coefficients.load_pressure_coefficients(Y, Z)
    coefficients = out_dict['coefficients']
    sign = out_dict['sign']
    
    gamma = get_gamma(coefficients, Y, Z, sign)
    p = rho * e * (gamma - 1)
    return p

def srinivasan_p_zero(rho_guess, h, p):
    """
    A wrapper around the srinivasan_p() function suitable for input into optimize.fsolve()
    to solve for the density.
    Used in calculate_p_rho_h().
    """
    
    e = h - p / rho_guess
    p_correlation = srinivasan_p(e, rho_guess)
    zero = p - p_correlation
    return zero

def calculate_p_rho_h(u1, p1, rho1, h1, rho2_guess):
    """
    Calculate the pressure, density and enthalpy behind a normal shock wave in inviscid equilibrium flow
    given the upstream pressure, density and temperature and an educated guess for downstream density.
    Only applicable to air, and only when it is considered a real gas mixture.

    :param u2: Upstream velocity.
    :param p1: Upstream pressure.
    :param rho1: Upstream density.
    :param rho2_guess: Guess for downstream density.

    :return return_dict: A dictionary for the downstream values of pressure, density and enthalpy.
    """
    
    rho2_guess_original = rho2_guess
    tolerance = 1E-6
    # Need to supply an initial value, just ensure that it's larger than tolerance.
    density_ratio_difference = 2 * tolerance

    # Added for refined guessing
    divergence = False
    divide_counter = 0
    multiply_counter = 0
    persistance = 10.
    # Choose a value of guess_change larger than 1.0
    guess_change = 1.05
    guess_range = numpy.power(guess_change, float(persistance))

    while density_ratio_difference > tolerance:
        
        rho1_to_rho2 = rho1 / rho2_guess
        # print 'rho1_to_rho2: ', rho1_to_rho2
        p2 = p2_shock_wave(p1, rho1, u1, rho1_to_rho2)
        h2 = h2_shock_wave(h1, u1, rho1_to_rho2)

        full_out = optimize.fsolve(srinivasan_p_zero, rho2_guess, args=(h2, p2), full_output=True)
        
        # We only want to use the value fsolve() spits out if the equations converged.
        if full_out[-1].startswith('The solution converged'):
            divergence = False
            rho2_guess = full_out[0]
        
        if full_out[-1].startswith('The iteration is not making good progress'):
            # print "We're diverging."
            divergence = True
        
        if divergence and divide_counter < persistance:
            rho2_guess = rho2_guess / guess_change
            divide_counter += 1
            # Reset rho2_guess to it's original value if division of rho2_guess only results in divergence.
            if divide_counter == persistance:                
                rho2_guess = rho2_guess_original

        if divergence and divide_counter == persistance and multiply_counter < persistance:
            rho2_guess = rho2_guess * guess_change
            multiply_counter += 1
            if multiply_counter == persistance:
                error_message = 'We have tried modifying the rho2 guess but still the numerical solution of ' \
                    'the coupled equations for p, rho and h diverges.'
                print error_message
                    
        rho1_to_rho2_new = rho1 / rho2_guess
        density_ratio_difference = numpy.abs(rho1_to_rho2_new - rho1_to_rho2)

    rho2 = rho2_guess
    return_dict = {'pressure': p2,
                   'density': rho2,
                   'enthalpy': h2}
    return return_dict

def srinivasan_T(p, rho):
    """
    Calculate the temperature of air, when considered a real gas mixture, given the pressure and density.

    :param p: The pressure of the air.
    :param rho: The density of the air.

    :return T: The temperature of the air.
    """

    rho0 = constants.rho0
    p0 = constants.p0
    T0 = constants.T0
    R = constants.R

    Y = numpy.log10(rho / rho0)
    X = numpy.log10(p / p0)
    Z = X - Y

    if Z <= 0.25 and -7.0 <= Y <= 3.0:
        T = p / (rho * R)
    elif Z > 0.25 and -7.0 <= Y <= 3.0:
        out_dict = correlation_coefficients.load_temperature_coefficients(Y, Z)
        coefficients = out_dict['coefficients']
        sign = out_dict['sign']
        gamma = get_gamma(coefficients, Y, Z, sign)    
        T = T0 * numpy.exp(numpy.log(10) * gamma)
    else:
        print 'Y, and therefore rho, is out of allowable range.'
        print 'Y: ', Y

    return T

def calculate_u(u1, rho1, rho2):
    """
    Calculate the velocity behind a normal shock wave in inviscid equilibrium flow given the
    upstream velocity and density and the downstream density.

    :param u1: The upstream velocity
    :param rho1: The upstream density.
    :param rho2: The downstream density.

    :return u2: The downstream velocity.
    """
    u2 = u1 * rho1 / rho2
    return u2
