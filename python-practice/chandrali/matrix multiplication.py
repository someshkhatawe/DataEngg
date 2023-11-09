# ********DAY 45********
# Python coding question:
#
# Given two matrix the task is that we will have to create a program to multiply two matrices in python.
# Examples:
# Input : X = [[1, 7, 3],
# [3, 5, 6],
# [6, 8, 9]]
# Y = [[1, 1, 1, 2],
# [6, 7, 3, 0],
# [4, 5, 9, 1]]
#
# Output : [55, 65, 49, 5]
# [57, 68, 72, 12]
# [90, 107, 111, 21]


x =[[1,7,3],
    [3,5,6],
    [6,8,9]]

y =[[1,1,1,2],
    [6,7,3,0],
    [4,5,9,1]]

f_matrix =[]
for i in range(len(x[0])):
    result = []
    for k in range(len(y[0])):
        sum = 0
        for j in range(0,len(y[0])-1):
            sum = sum + x[i][j] * y[j][k]
        result.append(sum)
    f_matrix.append(result)

print(f_matrix)
