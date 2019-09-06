# James Morrissey
# computingID: jpm9rk
# Approximate the integral using composite trapezoidal rule, composite midpoint rule, and composite Simpson's rule

import math


def function(x):
    """
    Return the value e^-x.

    :param x: (float)
    :return: return e^-x
    """
    return math.exp(-x)


TRUE_VALUE = 0.6321205588285577  # true value
H1 = 1/33  # step size defined by (b-a)/n
F_INIT = function(0)  # f(x_0)

total = 0
for i in range(1, 33):
    total += 2*function(i*H1)
# The resulting approximation from the composite trapezoidal rule, smallest n is 33
result1 = (total + F_INIT + function(1)) * H1/2


sum1 = 0
sum2 = 0
H2 = 1/4
# say n=20, m = 10

for j in range(1, 3):
    sum1 += 4 * function((2 * j - 1)*H2)

for j in range(1, 2):
    sum2 += 2 * function((2 * j)*H2)
# The resulting approximation from the composite Simpson's rule, smallest n is 4
result2 = (H2/3) * (F_INIT + sum1 + sum2 + function(1))

H3 = 1/46
sum3 = 0
for j in range(1,24):
    sum3 += 2 * H3 * function((2 * j-1) * H3)
# The resulting approximation from the composite midpoint formula, smallest n is 23
result3 = sum3

print('approximation using composite trapezoidal rule is', result1, ', for n = 33')
print('approximation using composite simpson rule is', result2, ', for n = 4')
print('approximation using composite midpoint rule is', result3, ', for n = 23')







