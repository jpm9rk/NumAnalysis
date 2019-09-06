# James Morrissey
# computingID: jpm9rk
# NOTE: adapt functions form is that recommended by the text

import math
ITERATION_MAX = 20
TOLERANCE = 5*10**-5
i = 0
def function(x):
    """
    Return Sin(sqrt(pi * x)).

    :param x:(float) x-value
    :return: function value
    """
    return math.sin((3.14159 * x)**(1/2))

def function2(u):
    return (2 * math.sin(u) * u) / 3.14159


def adapt(f, a, b, tolerance):
    fa = f(a)
    fc = f((b+a)/2)
    fb = f(b)
    sab = (b - a) * (fa + 4 * fc + fb)/6
    return adapt1(sab, fa, fc, fb, f, a, b, tolerance)


def adapt1(sab, fa, fc, fb, f, a, b, tolerance):
    global i
    i += 1
    c = (a + b)/2
    fd = f((a+c)/2)
    fe = f((c+b)/2)
    sac = (c-a) * (fa + 4 * fd + fc)/6
    scb = (b-c) * (fc + 4 * fe + fb)/6
    if abs(sac + scb - sab)/10 < tolerance:
        return sac+scb
    else:
        return adapt1(sac, fa, fd, fc, f, a, c, tolerance/2) + adapt1(scb, fc, fe, fb, f, c, b, tolerance/2)


print("Approximation using adaptive Simpson's rule is", adapt(function, 0, 1, 10**-7))
print(i + 2, 'iterations were needed')


# BELOW IS U-SUBSTITUTION
# BELOW IS U-SUBSTITUTION
# BELOW IS U-SUBSTITUTION
# BELOW IS U-SUBSTITUTION

print("Approximation using Simpson's rule with u-substitution is", adapt(function2, 0, 3.14159**(1/2), 10**-7))
print(i+2, 'iterations needed after u-substitution')

# So a greater number of iterations are needed for u-substitution









