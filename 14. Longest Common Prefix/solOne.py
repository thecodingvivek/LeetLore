strs = ["flower","flow","flight"]
mini = min(strs,key=len)
temp=mini
t=0
for i in range(len(mini)):
    for j in strs:
        if temp == j[:len(temp)]:
            t+=1
        else:
            t=0
            temp = temp[:-1]
            break
    if t == len(strs):
        print(temp)
        break

print("-1")

