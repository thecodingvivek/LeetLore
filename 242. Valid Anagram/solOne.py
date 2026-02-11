s = "raa"
t = "car"

sdict = {}
tdict = {}


for i in s:
    if i in sdict:
        sdict[i] += 1
    else:
        sdict[i]=0


for j in t:
    if j in tdict:
        tdict[j]+=1
    else:
        tdict[j]=0

if sdict == tdict:
    print(True)
