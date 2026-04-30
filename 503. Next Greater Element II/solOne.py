class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        hrmap=[-1] * n
        rstack=[]

        for index in range(2*n):
            while rstack and nums[index%n] > nums[rstack[-1]]:
                hrmap[rstack.pop()] = nums[index%n]
            
            if index < n:
                rstack.append(index)
        return hrmap

s=Solution()
print(s.nextGreaterElements(nums = [1,2,1]))
