intervals = [[4,7],[1,4]]
intervals.sort(key=lambda x:x[0])
newintervals=[]
i=0



while i<len(intervals)-1:
    if intervals[i+1][0]>=intervals[i][1]:
        newintervals.append([intervals[i][0],max(intervals[i][1],intervals[i+1][1])])
        i+=2
    else:
        newintervals.append([intervals[i][0],intervals[i][1]])
        i+=1

if(i==len(intervals)-1):
    newintervals.append(intervals[i])

print(newintervals)
    

