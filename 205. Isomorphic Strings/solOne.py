s = "bada"
t = "bada"

d= {}
inits = 0
initt = 0
ss = 0
tt=0

for i in s:
    if i in d:
        inits = (inits * 10) + d.get(i)
    else:
        ss+=1
        inits = (inits * 10) + ss
        d[i] = ss

d={}

for i in t:
    if i in d:
        initt = (initt * 10) + d.get(i)
    else:
        tt+=1
        initt = (initt * 10) + tt
        d[i] = tt

if inits == initt:
    print(True)
else:
    print(False)

