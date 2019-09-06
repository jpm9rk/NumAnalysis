# James Morrissey
# computingID: jpm9rk
# Use Newton's method to approximate all real roots
# Newton's Method Applied to e^x + x^2 - x - 4

import math


ITERATION_MAX = 100  # max number of iterations
p_initial = 1  # initial point used to find the positive root
p_initial_prime = -2  # initial point used to find the negative root
PRECISION = 10**(-6)  # define the stopping precision

def function(xvalue):  # the function we wish to find the roots of
    yvalue = math.exp(xvalue) + xvalue**2 - xvalue - 4
    return yvalue


def function_derivative(xvalue):  # derivative of the previous function
    yvalue = math.exp(xvalue) + 2*xvalue - 1
    return yvalue


def iteration_function(p):  # the iteration function for newtons method
    root_approximation = p - function(p)/function_derivative(p)
    return root_approximation


for i in range(ITERATION_MAX):  # converges to the positive root
    estimated_root = iteration_function(p_initial)
    estimated_error = abs(estimated_root - p_initial)
    print('the estimated root for iteration', i, 'is', estimated_root)
    print('         the absolute error approximation is', estimated_error)
    p_initial = estimated_root
    if estimated_error < PRECISION:  # stopping condition
        print('desired precision achieved')
        break


for i in range(ITERATION_MAX):  # converges to the negative root
    estimated_root = iteration_function(p_initial_prime)
    estimated_error = abs(estimated_root - p_initial_prime)
    print('the estimated root for iteration', i, 'is', estimated_root)
    print('         the absolute error approximation is', estimated_error)
    p_initial_prime = estimated_root
    if estimated_error < PRECISION:  # stopping condition
        print('desired precision achieved')
        break

# NOTE: Newton's method is highly dependent on the starting value, so I plotted the function to get an idea of where
# the roots were located, and used 2 separate but identical for loops
