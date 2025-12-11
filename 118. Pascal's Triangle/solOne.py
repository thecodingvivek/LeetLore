numRows = 5

triangle = [[1],[1,1]]
# if numRows==1:
#     # return [1]
# elif numRows ==2 :
#     # return triangle
temp=[]
for i in range(2,numRows):
    temp.append(1)
    for j in range(1,i):
        temp.append(triangle[i-1][j]+triangle[i-1][j-1])
    temp.append(1)

    triangle.append(temp)
    temp=[]



print(triangle)