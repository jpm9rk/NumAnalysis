# James Morrissey
# computingID: jpm9rk
# Perform 5 iterations of Newton's method 
# Newton's Method applied to x^7 = 3

ITERATION_MAX = 5  # setting the max number of iterations
p_initial = 1.5  # starting value p_0


def function(xvalue):
    yvalue = xvalue**7 - 3
    return yvalue


def function_derivative(xvalue):
    yvalue = 7* xvalue**6
    return yvalue

def iteration_function(p):
    root_approximation = p - function(p)/function_derivative(p)
    return root_approximation

for i in range(ITERATION_MAX):
    # if i == 0:
    #     p1 = p_initial
    # if i == 2:
    #     p2 = p_initial

    estimated_root = iteration_function(p_initial)
    print('the estimated root is', estimated_root, 'for iteration', i+1)
    print('     1: the absolute difference between p', i+1, 'and p', i, 'is', abs(estimated_root-p_initial))
    print('     2: the absolute difference between p', i+1, 'and the true root is', abs(estimated_root - 3**(1/7)))
    print('     3: the absolute difference between p', i, 'and the true root is', abs(p_initial - 3**(1/7)))
    ratio = abs(estimated_root - 3**(1/7))/abs(p_initial - 3**(1/7))**2
    print('     4: the value of the desired ratio is', ratio)
    p_initial = estimated_root


# Can see that the difference between p_n and the true root p is always smaller than the difference between p_n-1
# and the true root which is to be expected. This is an indication that our approximations to the root are getting
# better with each iteration. Additionally,the difference between p_n and p_n-1
# is always larger than the absolute difference between p_n and the true root p for the given starting approximation
# Computing the actual value of the ratio asked for shows that it is about 2.564
# After 5 iterations, the value of the ratio is about 2.56395 , clearly showing that
# it is trending toward 2.564
