matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

cstart = 0
cend = len(matrix)-1

while cstart<=cend:
    mid = (cstart+cend)//2

    if matrix[mid][0]>target:
        cend = mid-1
    else:
        cstart = mid+1

start = 0
end = len(matrix[cend])

while start<=end:
    mid = (start+end)//2

    if matrix[cend][mid] == target:
        print(matrix[cend][mid])
        break
    elif matrix[cend][mid]<target:
        start = mid+1
    else:
        end = mid - 1

print(-1)