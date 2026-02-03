arr = [2,3,4,7,11,12]
#     [0,1,2,3, 4]

k = 2


start = 0
end = len(arr) - 1

while start<end:
    mid = (start+end)//2

    if (arr[mid] -  (mid + 1)) < k:
        start = mid + 1
    else:
        end = mid - 1


print(start+k) 







