nums = [3,1,-2,-5,2,-4]
temp = [0 for i in nums]

p=0
j=1


for i in nums:
    if i >0:
        temp[p] = i
        p+=2
    else:
        temp[j] = i
        j+=2



print(temp)
