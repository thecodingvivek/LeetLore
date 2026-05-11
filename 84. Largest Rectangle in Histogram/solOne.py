class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        index=[n]*n
        stack = []
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                index[stack.pop()] = i
            stack.append(i)


        stack=[]
        lindex = [-1]*n
        for i in range(n-1,-1,-1):
            while stack and heights[i] < heights[stack[-1]]:
                lindex[stack.pop()] = i
            stack.append(i)        

        maxi = 0
        for i in range(n):
            width = index[i] - lindex[i] - 1
            area = heights[i] * width
            maxi = max(maxi, area)

        return maxi
                



s = Solution()
print(s.largestRectangleArea(heights = [2,1,5,6,2,3]))
                