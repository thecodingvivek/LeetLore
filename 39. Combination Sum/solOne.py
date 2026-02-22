candidates = [2]
target = 1
def combinationSum(candidates, target):
    final = []
    def helper(index,stack,total):
        if total == target:
            final.append(list(stack))
            return

        if total > target or index >= len(candidates):
            return
        
        stack.append(candidates[index])
        helper(index,stack,total+candidates[index])
        stack.pop()

        helper(index+1,stack,total)


    helper(0,[],0)
    print(final)



combinationSum(candidates,target)