num = "3"

for i in range(len(num)-1,-1,-1):
    if int(num[i])%2 != 0:
        print(num[:i+1])
    
print(-1)