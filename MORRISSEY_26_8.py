# James Morrissey
# computingID: jpm9rk
# Perform 10 iterations to approximate the fixed point of g(x) = ln( 4 + x - x^2 )


import math

ITERATION_MAX = 10

p_initial = 2
counter = 0


def aitkens_function(p1,p2,p3):   # p1 = p_n, p2 = p_n-1, p3 = p_n-2
    p_hat = p1 - ((p1 - p2)**2)/(p1 + p3 - 2*p2)
    return p_hat


def function(xvalue):
    yvalue = math.log(4 + xvalue - xvalue**2)
    return yvalue


for i in range(ITERATION_MAX):
    estimated_root = function(p_initial)  # first iteration gives p_1, need up to p_3 to use aitken
    # print('ITERATION', i+1, ' of fixed position gives a root estimate of', estimated_root)
    if i == 0:
        p1 = estimated_root  # p1 becomes the root estimation on the first iteration
    if i == 1:
        p2 = estimated_root  # p2 becomes the root estimation on the second iteration
    p_initial = estimated_root
    if i > 1:
        p3 = estimated_root
        a_root_estimation = aitkens_function(p3,p2,p1)
        error_estimate = abs(a_root_estimation - 1.2886779668238684115)
        if counter > 0:
            error_ratio = error_estimate/error_estimate_prime
            print('the ratio of e_n+1 over e_n is', error_ratio)
        error_estimate_prime = error_estimate
        print('     aitkens estimate for iteration', i+1, 'of fixed point method is',a_root_estimation)
        p1 = p2  # for the next iteration, p_n-2 = p_n-1
        p2 = p3  # for the next iteration, p_n-1 = p_n

        counter += 1


# |e_n+1|/|e_n| is approaching a constant (which confirms linear convergence) that is about equal to
# 0.189 (which is our lambda value)
