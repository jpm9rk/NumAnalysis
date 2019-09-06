# James Morrissey
# computingID: jpm9rk
# find the root of x^7-3 on the interval (1,2) using 7 iterations of the secant method

import math

ITERATION_MAX = 10

p_zero = 2
p_one = 1

def function(xvalue):
    yvalue = xvalue**7 - 3
    return yvalue

for i in range(ITERATION_MAX):  # first iteration of this finds p_2
    estimated_root = p_one - function(p_one)*(p_one - p_zero)/(function(p_one) - function(p_zero))  # this is p2
    print('the estimated root for iteration', i+1, 'is', estimated_root)
    if i > -1:
        print('     1: the absolute difference between p', i+2, 'and p', i+1, 'is', abs(estimated_root-p_one))
        print('     2: the absolute difference between p', i+2, 'and the true root is', abs(estimated_root - 3**(1/7)))
        print('     3: the absolute difference between p', i+1, 'and the true root is', abs(p_one-3**(1/7)))
        ratio = abs((estimated_root - p_one))/abs((p_one - p_zero))**1.618
        print('     the desired ratio is',ratio)
    p_zero = p_one
    p_one = estimated_root

# Inspection of the output shows that after the initial iteration, the absolute difference between
# p_n and the actual value of the root becomes the smallest of the three quantities. As expected, p_n is always
# closer to the true value of the root than p_n-1, indicating that our approximations to the root are getting
# better with each iteration
# the actual value of the ratio asked for is about 1.79
# doing 10 iterations of the secant method yields what is effectively 0 difference between estimated root
# and the actual one. As shown if ITERATION_MAX is changed to 10, the last value for the ratio is 1.765 showing
# that this ratio is tending toward 1.79
