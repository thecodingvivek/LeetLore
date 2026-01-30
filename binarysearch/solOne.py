l=[2,3,4,5,6,7,8]


target = 3
start = 0
end = len(l)-1

while start<=end:
    mid =(start + end)//2
    if l[mid]==target:
        print(mid)
        break
    elif l[mid]>target:
        end = mid - 1
    elif l[mid]<target:
        start = mid + 1

    
    
    

