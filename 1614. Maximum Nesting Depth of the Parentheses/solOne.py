s = "("
stack = []
maxi = 0
for i in s:
    if i == "(":
        stack.append("(")
    elif i == ")":
        if len(stack)>maxi:
            maxi = len(stack)
        stack.pop()

print(maxi)
