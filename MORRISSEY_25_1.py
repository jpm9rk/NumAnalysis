# James Morrissey
# computingID: jpm9rk
# Use the secant method to determine the fourth approximation to the root on the interval (0,1)
# Find the zeros of cosx-x = 0 using the secant method

import math

ITERATION_MAX = 4  # max number of iterations

p_zero = 1 # initial values
p_one = 0


def function(xvalue):  # defining the function
    yvalue = math.cos(xvalue) - xvalue
    return yvalue


for i in range(ITERATION_MAX):
    estimated_root = p_one - function(p_one)*(p_one - p_zero)/(function(p_one) - function(p_zero))
    p_zero = p_one
    p_one = estimated_root
    print('the estimated root for iteration', i+1, 'is', estimated_root)
