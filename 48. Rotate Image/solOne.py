matrix = [[1,2,3],[4,5,6],[7,8,9]]


for i in range(len(matrix)):
    for j in range(i+1,len(matrix[0])):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

for k in range(len(matrix)):
    s = 0
    e = len(matrix[i]) - 1
    while s<e:
        matrix[k][s],matrix[k][e] = matrix[k][e],matrix[k][s]
        s+=1
        e-=1


print(matrix)
        