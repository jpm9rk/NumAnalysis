# James Morrissey
# computingID: jpm9rk
# Solve the nonlinear system of equations using Newton's method and Broyden's method

from operator import add
from operator import sub
x1 = 0
x2 = 0
PRECISION = 5 * 10**-6
ITERATION_MAX = 8
ITERATION_MAX_PRIME = 1
v_old = [0, 0]
v_new = [0, 0]
difference_vec = [0, 0]
x_initial = [7, 2]
x_approx = [0, 0]
inverse_times_y = [0, 0]
delta_t_times_inverse = [0, 0]
subtraction = [0, 0]

def jacobian(x_initial):
    """
    Evaluate the Jacobian at the approximation to x.

    :param x_initial:(vec) the current approximation to x
    :return:(matrix) the value of the Jacobian matrix evaluated at x
    """
    jacobian_matrix = [[-1/3, 1], [2 * x_initial[0]/(x_initial[0]**2 + 1)**2, -1/2]]
    return jacobian_matrix


def f_vector(x_initial):
    """
    Evaluate the F vector at the current approximation to x.

    :param x_initial:(vec) the current approximation to x
    :return: (vec) the value of the F vector evaluated at x
    """
    f_vector_evaluation = [-1/3 * x_initial[0] + x_initial[1], x_initial[0]**2/(1 + x_initial[0]**2) - 1/2 * x_initial[1]]
    return f_vector_evaluation


for k in range(ITERATION_MAX):
    the_f_vector = f_vector(x_initial)
    the_jacobian_matrix = jacobian(x_initial)
    for pass_num in range(0, 1):
        for row in range(pass_num + 1, 2):  # pass_num is 1 for first loop, as is row
            m = - the_jacobian_matrix[row][pass_num] / the_jacobian_matrix[pass_num][pass_num]  # row starts as row 2
            the_jacobian_matrix[row][pass_num] = 0
            for col in range(pass_num + 1, 2):
                the_jacobian_matrix[row][col] = the_jacobian_matrix[row][col] + m * the_jacobian_matrix[pass_num][col]
    # print('reduced matrix', the_jacobian_matrix)
    v_new[1] = -the_f_vector[1]/the_jacobian_matrix[1][1]
    v_new[0] = (-the_f_vector[0] - the_jacobian_matrix[0][1] * v_new[1])/the_jacobian_matrix[0][0]
    v_abs = [abs(v_new[0]), abs(v_new[1])]
    vector_norm = v_abs[1]
    if v_abs[1] < v_abs[0]:
        vector_norm = v_abs[0]
    # print('v new ',v_new)
    x_approx = list(map(add, x_initial, v_new))
    if vector_norm < PRECISION:
        print('Desired precision achieved after',k+1, ' iterations, approximation to x is:', x_approx)
        break
    x_initial = x_approx


# PART B STARTS HERE
# PART B STARTS HERE
# PART B STARTS HERE
# PART B STARTS HERE
# The following is performed using the Broyden method




total = 0

jacobian_inverse = [[-3.10430, -6.20861], [-0.03477, -2.06954]]  # A_0^-1
the_f_vector = f_vector(x_initial)  # F(x^(0))
for j in range(2):  # loop to calculate v^(0)
    for i in range(2):
        total += -1 * jacobian_inverse[j][i] * f_vector(x_initial)[i]
    v_old[j] = total
    total = 0
x_approx = list(map(add, x_initial, v_old))

for k in range(ITERATION_MAX):
    delta = v_old
    y_vector = list(map(sub, f_vector(x_approx),f_vector(x_initial)))
    for j in range(2):
        for i in range(2):
            total += jacobian_inverse[j][i] * y_vector[i]
        inverse_times_y[j] = total
        total = 0
    for g in range(2):  # calculates delta transpose * inverse
        # g q
        for f in range(2):
            # g=1, f=0,1
            total += delta[f] * jacobian_inverse[f][g]
        delta_t_times_inverse[g] = total
        total = 0
    # the following calculates delta transpose * inverse * yvec
    delta_inverse_y = delta_t_times_inverse[0] * y_vector[0] + delta_t_times_inverse[1] * y_vector[1]
    subtraction = list(map(sub, delta, inverse_times_y))
    numerator = subtraction[0] * delta_t_times_inverse[0] + subtraction[1] * delta_t_times_inverse[1]
    fraction = numerator/ delta_inverse_y
    # Calculating the new elements of the inverse jacobian
    jacobian_inverse[0][0] = jacobian_inverse[0][0] + fraction
    jacobian_inverse[1][1] = jacobian_inverse[1][1] + fraction
    jacobian_inverse[0][1] = jacobian_inverse[0][1] + fraction
    jacobian_inverse[1][0] = jacobian_inverse[1][0] + fraction
    for j in range(2):  # calculates A^-1 * y
        for i in range(2):
            total += -1*jacobian_inverse[j][i] * f_vector(x_approx)[i] # calculates -A^-1 * F(x^(k))
        v_new[j] = total
        total = 0
    v_abs = [abs(v_new[0]), abs(v_new[1])]
    vector_norm = v_abs[1]
    if v_abs[1] < v_abs[0]:
        vector_norm = v_abs[0]
    x_initial = x_approx
    v_old = v_new
    x_approx = list(map(add, x_approx, v_new))
    print(x_approx)
    if vector_norm < PRECISION:
        print('Desired precision using broyden method'
              ' achieved after', k+2, 'iterations, approximation to x is:', x_approx)
        break







