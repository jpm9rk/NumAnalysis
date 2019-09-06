# James Morrissey
# computingID: jpm9rk
# Perform 7 iterations of fixed point iteration scheme and numerically confirm order of convergence
# fixed point scheme for g(x) = 2x(1-x) which has fixed points at x=0,1/2
# expectation is that the sequence will converge to 1/2 with quadratic convergence
# implies e_n = lambda*e_(n-1)^2 where lambda is between 0 and 1
# this is super-linear convergence so a stopping condition is when |e_n| > |p_n  - p_n-1|

ITERATION_MAX = 7  # definition of the max number of iterations
initial_value = 0.1  # defining p_0
counter = 0


def g_function (xvalue):  # defining the iteration function
    yvalue = 2 * xvalue * (1-xvalue)
    return yvalue


for i in range(ITERATION_MAX):  # setting number of iterations
    estimated_root = g_function(initial_value)  # evaluate g at p_n which becomes an estimate for location
                                                # of the next root
    estimated_error = estimated_root - initial_value
    if i > 0:  # need e_n+1 to calculate e_n+1 / e_n
        print('             the ratio of |e_n|/|e_n-1| is', abs(estimated_error)/abs(estimated_error_prime)**2)
    estimated_error_prime = estimated_error  # dummy variable for use in calculating error ratio
    print('the estimated root is', estimated_root, ' with an estimated '
                                                    'error of ', estimated_error, 'and has been achieved after'
                                                                                , i+1, 'iteration(s)')

    initial_value = estimated_root              # p_(n+1) becomes p_n for the next iteration

#  the first few error estimates are not the best but starting from the 4th error estimate the
#  error estimates are approaching quadratic
#  order of convergence e_n+1 = 2 * e_n
#  So the order of convergence is not quite quadratic, as 2 > 1, but we are close to quadratic convergence
