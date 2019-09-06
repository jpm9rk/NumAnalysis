# James Morrissey
# computingID: jpm9rk
# Solve the linear system of equations using conjugate gradient, Gauss-Seidel, and Jacobi methods

from operator import add

ITERATION_MAX = 50
TOLERANCE = 5 * 10**-7
total = 0
value = 0

matrix = [[4, 1, 1, 1], [1, 3, -1, 1], [1, -1, 2, 0], [1, 1, 0, 3]]   # defining the A matrix

residual_init = [-33/2, -1/2, -17/2, -27/2]  # the initial value of the residual
d_vec = [33/2, 1/2, 17/2, 27/2]
delta = 527
u_vec = [0, 0, 0, 0]  # initializing this to be used later on
x_old = [0, 0, 0, 0]  # the initial approximation to x
x_new = []
residual = [0, 0, 0, 0]
u_vec_times_lambda = [0, 0, 0, 0]


for m in range(ITERATION_MAX):
    for j in range(4):  # loop to calculate matrix-vector product u = Ad
        for i in range(4):
            total += matrix[j][i] * d_vec[i]
        u_vec[j] = total
        total = 0
    # print('u vec', u_vec)
    # print('d vec', d_vec)
# EVERYTHING ABOVE THIS LINE IS RIGHT
    for k in range(4):   # loop to calculate d^(m)Tu
        value += (d_vec[k] * u_vec[k])
    # print('value', value)
    lambda_value = delta / value   # dividing delta by the value in previous loop gives lambda value
    # print('lambda value', lambda_value)
    d_vec_times_lambda = [i * lambda_value for i in d_vec]  # vector obtained by multiplying d_vec by lambda
    x_new = list(map(add, x_old, d_vec_times_lambda))  # calculate the new approximation to x
    u_vec_times_lambda = [i * lambda_value for i in u_vec]  # vector obtained by multiplying u_vec by lambda
    # print(u_vec_times_lambda)
    residual = list(map(add, residual_init, u_vec_times_lambda)) # calculate the new approximation for the residual
    # print('residual', residual)
    delta_new = residual[0]**2 + residual[1]**2 + residual[2]**2 + residual[3]**2
    # print('delta new', delta_new)
    if delta_new**(1/2) < TOLERANCE:
        print('Desired tolerance achieved after', m+1,'iterations. The approximation to x is ', x_new, '\n')
        break
    # else:
        # print('convergence not ahieved, x approximation is', x_new)
    alpha = delta_new / delta
    # print('alpha', alpha)
    d_vec_times_alpha = [i * alpha for i in d_vec]
    residual_minus = [-1 * i for i in residual]
    d_vec = list(map(add, residual_minus, d_vec_times_alpha))
    # print('d vec new', d_vec)
    # print(d_vec)
    # print('residual', residual)
    x_old = x_new  # x^(m+1) becomes x^(m) for the next iteration
    residual_init = residual  # r^(m+1) becomes r^(m) for the next iteration
    delta = delta_new  # delta^(m+1) becomes delta^(m) for the next iteration
    value = 0

difference_vec = []
x_old = [0, 0, 0, 0, 0]  # initialize the first approximation
x_new = [0, 0, 0, 0, 0]  # initialize what will store subsequent approximations
difference_vec = [0, 0, 0, 0, 0]

for i in range(ITERATION_MAX):
    x_new[0] = (1/4) * (33/2 - x_old[1] - x_old[2] - x_old[3])
    x_new[1] = (1/3) * (1/2 - x_old[0] + x_old[2] - x_old[3])
    x_new[2] = (1/2) * (17/2 - x_old[0] + x_old[1])
    x_new[3] = (1/3) * (27/2 - x_old[0] - x_old[1])
    for j in range(4):
        difference_vec[j]= (abs(x_new[j] - x_old[j]))  # create a vector that stores the difference between
        # the old and new approximations
    vec_norm = max(difference_vec)  # stores the value of the error
    # print('the error for iteration', i+1, 'is', vec_norm)
    if vec_norm < TOLERANCE:  # break the loop if the precision is within desired range
        print('Desired precision using Jacobi method achieved after', i+1, 'iterations, and is as follows:')
        for k in range(4):
            print(x_new[k], end='  ')
        break
    for l in range(4):
        x_old[l] = x_new[l]  # the components of

print()
print()
# SOLVING SYSTEM USING GAUSS-SEIDEL METHOD

difference_vec = []
x_old = [0, 0, 0, 0, 0]  # initialize the first approximation
x_new = [0, 0, 0, 0, 0]  # initialize what will store subsequent approximations
difference_vec = [0, 0, 0, 0, 0]

for i in range(ITERATION_MAX):
    x_new[0] = (1/4) * (33/2 - x_old[1] - x_old[2] - x_old[3])
    x_new[1] = (1/3) * (1/2 - x_new[0] + x_old[2] - x_old[3])
    x_new[2] = (1/2) * (17/2 - x_new[0] + x_new[1])
    x_new[3] = (1/3) * (27/2 - x_new[0] - x_new[1])
    for j in range(4):
        difference_vec[j]= (abs(x_new[j] - x_old[j]))  # create a vector that stores the difference between
        # the old and new approximations
    vec_norm = max(difference_vec)  # stores the value of the error
    # print('the error for iteration', i+1, 'is', vec_norm)
    if vec_norm < TOLERANCE:  # break the loop if the precision is within desired range
        print('Desired precision using Gauss-Seidel method achieved after', i+1, 'iterations, and is as follows:')
        for k in range(4):
            print(x_new[k], end='  ')
        break
    for l in range(4):
        x_old[l] = x_new[l]

# READ ME
# READ ME
# READ ME
# Clearly the conjugate gradient method in this case is superior in terms of iterations needed to achieve convergence.
# The Gauss-Seidel method required 5 times the amount of iterations as conjugate gradient to achieve
# convergence, and the Jacobi method was even worse, requiring twice as many iterations as Gauss-Seidel


