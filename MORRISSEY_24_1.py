# James Morrissey
# computingID: jpm9rk


# Perform Newton's method for the function cosx-x = 0
# Newton's method is defined by g(x) = x - f(x)/f'(x)
import math

ITERATION_MAX = 4
p_initial = 1

def function(xvalue):
    yvalue = math.cos(xvalue)-xvalue
    return yvalue


def function_derivative(xvalue):
    yvalue = -1*math.sin(xvalue)-1
    return yvalue


def iteration_function(p):
    root_approximation = p - function(p)/function_derivative(p)
    return root_approximation

for i in range(ITERATION_MAX):
    estimated_root = iteration_function(p_initial)
    print('the estimated root is', estimated_root, 'for iteration', i+1)
    p_initial = estimated_root

