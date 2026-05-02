class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        MODULO = 10**9 + 7
        n=len(arr)
        left = [0] * n
        stack = []

        for i in range(0,len(arr)):
            count=1
            while stack and stack[-1][0] > arr[i]:
                count+=stack.pop()[1]
            left[i] = count

            stack.append((arr[i],count))

        right = [0]*n
        stack=[]

        for i in range(n-1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            right[i] = count
            stack.append((arr[i], count))

        result = 0
        for i in range(len(arr)):
            result += arr[i] * left[i] * right[i]
            result = result%MODULO

        return result            

        





s=Solution()
print(s.sumSubarrayMins(arr = [3,1,2,4]))