# James Morrissey
# computingID: jpm9rk
# Perform 10 iterations of the secant method on the function x(1-cosx)
# which has a zero at x = 0 ---> determine if convergence is quadratic

import math

ITERATION_MAX = 10
p_zero = -1
p_one = 2

def function(xvalue):
    yvalue = xvalue * (1 - math.cos(xvalue))
    return yvalue

for i in range(ITERATION_MAX):
    estimated_root = p_one - function(p_one)*(p_one - p_zero)/(function(p_one) - function(p_zero))  # this is p2
    print('the estimated root for iteration', i+1, 'is', estimated_root)
    if i > 0:
        print('     the error of e_n / e_n+1 is,', abs(estimated_root)/abs(estimated_error))
    estimated_error = estimated_root
    p_zero = p_one
    p_one = estimated_root

# Having been told that the actual root is at x = 0 and by inspection of the
# root approximations, it is clear that we only have linear convergence. Each error value is equal to the
# previous error multiplied by a value between 0 and 1
# Additional verification is shown by the fact that the ratio of |e_n+1|\|e_n| approaches a constant
