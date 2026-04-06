class Solution(object):
    def subsetsWithDup(self, nums):
        result = []
        nums.sort()
        def helper(index,stack):

            result.append((stack))

            
            for i in range(index,len(nums)):
                if index!=i and nums[i]==nums[i-1]:
                    continue

                stack.append(nums[i])
                helper(i+1,list(stack))
                stack.pop()           

        helper(0,[])
        return result


nums = [0]

s=Solution()
print(s.subsetsWithDup(nums))