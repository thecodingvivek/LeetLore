class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        def helper(index,temp,currsum):
            if currsum == target:
                result.append(temp)
                return

            if currsum > target or index >= len(candidates):
                return
            
            temp.append(candidates[index])
            helper(index,list(temp),currsum+candidates[index])
            temp.pop()
            helper(index+1,list(temp),currsum)


            
            
        helper(0,[],0)
        return result


s = Solution()
print(s.combinationSum([2,3,6,7],7))