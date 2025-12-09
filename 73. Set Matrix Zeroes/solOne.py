matrix = [[1,1,1],[1,0,1],[1,1,1]]
l = []
row = [0 for h in range(len(matrix[0]))]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            l.append((i,j))
    

for tup in l:
    matrix[tup[0]] = row
    for t in range(len(matrix)):
        matrix[t][tup[1]] = 0

print(matrix)
            