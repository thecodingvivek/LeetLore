num = [3,2,4]
target = 6


newnums=[]

for i,j in enumerate(num):
    newnums.append([i,j])


newnums.sort(key=lambda x:x[1])
num.sort()

firstPointer = 0
lastPointer = len(num)-1
result=[]


while lastPointer>firstPointer:
    sum=newnums[firstPointer][1]+newnums[lastPointer][1]
    if sum== target:
        result.extend([newnums[firstPointer][0],newnums[lastPointer][0]])
        break
    elif sum>target:
        lastPointer-=1
    else:
        firstPointer+=1

    
