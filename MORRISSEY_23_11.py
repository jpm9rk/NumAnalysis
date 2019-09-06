# James Morrissey
# computingID: jpm9rk
# Use a fixed point iteration scheme to find the fixed point of g(x)=exp(-x^2) on the interval [0,1]
import math




ITERATION_MAX = 1000 # max number of iterations the algorithm will run through
PRECISION = 5 * 10**-7
initial_value = 0 # seting p_0 value for the algorithm
counter = 0


def g_function(xvalue):  
    """Return exp(-x^2)."""
    yvalue = math.exp(-(xvalue**2))
    return yvalue


def g_prime(p1, p2, p3):  # defines the approximation of the derivative of g(x) at p,p1 = p_n ,p2 = p_n-1 ,p3 = p_n-2
    derivative = (p1-p2)/(p2-p3)
    return derivative


for i in range(ITERATION_MAX):  # note that the first iteration of this loop gives p_1

    if counter == 1:
        break
    estimated_root = g_function(initial_value)  # calculates p_n based on p_n-1
    print('estimated root for iteration', i + 1, 'is', estimated_root)
    # if i > 2:
    if i == 0:
        g1 = estimated_root  # stores the p_1 value
        # print(g1)
    if i == 1:
        g2 = estimated_root # stores the p_2 value
        # print(g2)
    if i > 1:  # p3 has just been calculated at the beginning of this iteration
        g3 = estimated_root
        # print(g_prime(g1,g2,g3))
        estimated_error = abs(g_prime(g3,g2,g1)/(g_prime(g3,g2,g1)-1))*abs((g3-g2))  # calculates the error for pn-2
                                                                                     # pn-1, pn,kk
        g1 = g2  # stores the value for p_n-1 in what will be p_n-2 for the next iteration
        g2 = g3  # stores the value for p_n in what will be p_n-1 for the next iteration
        print('         estimated error for iteration', i+1, 'is', estimated_error)
        if estimated_error < PRECISION and counter != 1:
            print('precision has been achieved after', i+1, 'iterations')
            counter += 1
    initial_value = estimated_root  # assigns the p_n-1 value to used to calculate p_n







