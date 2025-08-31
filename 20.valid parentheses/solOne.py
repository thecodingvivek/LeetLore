s="]"
stack=[]
d={"(":")","{":"}","[":"]"};



for i in s:
    if i in d.values():
        if len(stack)>1:
            print("not consistent")
        if d[stack.pop()] != i:
            print("not consistent!")

        
    else:
        stack.append(i)


if len(stack) == 0:
    print("consistent")
else:
    print("not consistent")

