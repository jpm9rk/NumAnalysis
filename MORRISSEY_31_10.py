# James Morrissey
# computingID: jpm9rk
# Solve the system using Gaussian elimination with back substitution


print('PART A')
matrix = [[3.02, -1.05, 2.53, -1.61], [4.33, 0.56, -1.78, 7.23], [-0.83, -0.54, 1.47, -3.38]]



# 1st row of matrix has first index 0, second row has first index 1, third row has first index 2

for pass_num in range(0,2):
    for row in range(pass_num+1, 3):  # pass_num is 1 for first loop, as is row
        m = - matrix[row][pass_num]/matrix[pass_num][pass_num]  # row starts as row 2
        matrix[row][pass_num] = 0
        for col in range(pass_num + 1, 4):
            matrix[row][col] = matrix[row][col] + m * matrix[pass_num][col]
print('reduced matrix', matrix)

x_vec = [0, 0, 0, matrix[]
x_vec_original = [0, 0, 0]

print('x component 3 is',x_vec[2])
print('hi')
for row in range(1,-1,-1):  # includes row 2 and row 1
    sum = matrix[row][3]  # sum is equal to the b in row 2 or row 1
    for col in range(row+1, 3):  # col 3 and col 2
        # print('this is col', col)
        sum = sum - matrix[row][col] * x_vec[col]
    x_vec[row] = sum / matrix[row][row]
    print('x component',row+1, 'is', x_vec[row])

matrix = [[3.02, -1.05, 2.53, -1.61], [4.33, 0.56, -1.78, 7.23], [-0.83, -0.54, 1.47, -3.38]]
print('')
print('PART B')
# START OF PART B

matrix = [[3.01, -1.05, 2.53, -1.61], [4.33, 0.56, -1.78, 7.23], [-0.83, -0.54, 1.47, -3.38]]

for pass_num in range(0,2):
    for row in range(pass_num+1, 3):  # pass_num is 1 for first loop, as is row
        m = - matrix[row][pass_num]/matrix[pass_num][pass_num]  # row starts as row 2
        matrix[row][pass_num] = 0
        for col in range(pass_num + 1, 4):
            matrix[row][col] = matrix[row][col] + m * matrix[pass_num][col]

x_vec = [0, 0, (matrix[2][3]/matrix[2][2])]

print('x component 3 is',x_vec[2])

for row in range(1,-1,-1):  # includes row 2 and row 1
    sum = matrix[row][3]  # sum is equal to the b in row 2 or row 1
    for col in range(row+1, 3):  # col 3 and col 2
        # print('this is col', col)
        sum = sum - matrix[row][col] * x_vec[col]
    x_vec[row] = sum / matrix[row][row]
    print('x component',row+1, 'is', x_vec[row])

print('')
print('x component 3 has changed by', abs(((1.0000000000001137 + x_vec[2])/1.0000000000001137))*100, 'percent')
print('x component 2 has changed by', abs((-1.9999999999997025+x_vec[1])/-1.9999999999997025)*100, 'percent')
print('x component 1 has changed by', abs((x_vec[0]-0.9999999999999917)/0.9999999999999917)*100, 'percent \n')

print("PART C")
# START OF PART C

matrix = [[3.02, -1.05, 2.53, -1.61], [4.33, 0.56, -1.78, 7.23], [-0.83, -0.54, 1.47, -3.39]]

for pass_num in range(0,2):
    for row in range(pass_num+1, 3):  # pass_num is 1 for first loop, as is row
        m = - matrix[row][pass_num]/matrix[pass_num][pass_num]  # row starts as row 2
        matrix[row][pass_num] = 0
        for col in range(pass_num + 1, 4):
            matrix[row][col] = matrix[row][col] + m * matrix[pass_num][col]

x_vec = [0, 0, (matrix[2][3]/matrix[2][2])]

print('x component 3 is',x_vec[2])

for row in range(1,-1,-1):  # includes row 2 and row 1
    sum = matrix[row][3]  # sum is equal to the b in row 2 or row 1
    for col in range(row+1, 3):  # col 3 and col 2
        # print('this is col', col)
        sum = sum - matrix[row][col] * x_vec[col]
    x_vec[row] = sum / matrix[row][row]
    print('x component',row+1, 'is', x_vec[row])

print('')
print('x component 3 has changed by', abs(((x_vec[2] + 1.0000000000001137)/1.0000000000001137))*100, 'percent')
print('x component 2 has changed by', abs((x_vec[1]-1.9999999999997025)/-1.9999999999997025)*100, 'percent')
print('x component 1 has changed by', abs((x_vec[0]-0.9999999999999917)/0.9999999999999917)*100, 'percent')








