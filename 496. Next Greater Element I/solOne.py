class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        hmap={}

        for num in nums2:
            while stack and num > stack[-1]:
                hmap[stack.pop()] = num
        
            stack.append(num)

        while stack:
            hmap[stack.pop()] = -1

        return [hmap[n] for n in nums1]







s = Solution()
print(s.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
            