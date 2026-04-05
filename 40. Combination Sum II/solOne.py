candidates = [2,5,2,1,2]
target = 5

def combinationSum2(candidates, target):
    final = []
    candidates.sort()
    def helper(index,stack,total):
        if total == target:
            final.append(stack)
            return
        
        if total > target or index >= len(candidates):
            return

        for i in range(index,len(candidates)):
            if i>index and candidates[i-1] == candidates[i]:
                continue
            stack.append(candidates[i])
            helper(i+1,list(stack),total+candidates[i])
            stack.pop()
        
    helper(0,[],0)
    return (final)
        
        
print(combinationSum2(candidates,target))