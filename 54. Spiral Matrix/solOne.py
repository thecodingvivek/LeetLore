matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
arr=[]

sr = 0
er = len(matrix)
sc = 0
ec = len(matrix[0])

while sr<er and sc< ec:
    for i in range(sc,ec):
        arr.append(matrix[sr][i])
    
    for j in range(sr+1,er):
        arr.append(matrix[j][ec-1])
    
    if sr < er-1:
        for k in range(ec-2,sc-1,-1):
            arr.append(matrix[er-1][k])

    if sc < ec-1:
        for l in range(er-2,sr,-1):
            arr.append(matrix[l][sc])


    sr+=1
    er-=1
    sc+=1
    ec-=1


print(arr)

# now prints: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

