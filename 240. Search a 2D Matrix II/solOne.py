matrix = [[2]]
target = 5

row = 0
column = len(matrix[0]) - 1

while row<len(matrix) and column>=0:
    if matrix[row][column] == target:
        print(row,column)
        break
    elif matrix[row][column] > target:
        column -=1
    else:
        row+=1

print(-1)