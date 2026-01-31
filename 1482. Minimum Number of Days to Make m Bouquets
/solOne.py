bloomDay = [7,7,7,7,12,7,7]
m = 2
k =3


totalflowers = m * k
if totalflowers > len(bloomDay):
    print(-1)
    exit()

start = 1
end = max(bloomDay)
mini = float('inf')

def findadj(mid):
    nofm=0
    count = 0

    for i in bloomDay:
        if i - mid <= 0:
            count+=1
        else:
            count=0

        if count == k:
            nofm+=1
            count=0

    return nofm 
            

while start<=end:
    mid = (start+end)//2
    
    nofm=findadj(mid)
    if nofm >= m:
        mini = mid
        end = mid - 1
    else:
        start = mid + 1

print(mini)
