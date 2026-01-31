weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

start = max(weights)
end = sum(weights)

def getDays(mid):
    days = 1
    curr = 0
    for i in weights:
        if curr + i > mid:
            days+=1
            curr=0
        curr+=i

    return days
    
while start<end:
    mid = (start+end)//2
    da = getDays(mid)
    if da > days:
        start = mid+1
    else:
        end = mid
        

print(start)

