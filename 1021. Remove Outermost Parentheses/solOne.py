s = "(()())(())"
balance = 0
f=""
for i in s:
    if i == '(':
        if balance > 0:
            f+=i
        balance+=1
    else:
        balance -=1
        if balance > 0:
            f+=i
         
    


print(f)