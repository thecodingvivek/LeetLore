s = "abcde"
goal = "abcde"

for i in range(len(goal)-1,-1,-1):
    pre = s[i:]
    post = s[:i]
    if pre+post == goal:
        print(True)
        break
print(False)