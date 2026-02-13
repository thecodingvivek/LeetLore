s = "the sky is blue"
f=""
j = len(s)-1

while j >=0:
    while s[j] == " ":
        j-=1

    i = j

    while i>=0 and s[i] != " ":
        i-=1

    if f == "":
        f += s[i+1:j+1]
    else:
        f+=  " " + s[i+1:j+1]


    j = i




print(f)

