# James Morrissey
# computingID: jpm9rk
# Solve the system using Gaussian elimination and partial pivoting


matrix = [[2, 3, 1, -4], [4, 2, 4, 9], [3, 4, 6, 0]]
row_vector = [0, 1, 2]

# first pass find max of matrix[0][0] [1][0] [2][0]

for pass_num in range(0,2):
    print('start of pass', pass_num + 1)
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
