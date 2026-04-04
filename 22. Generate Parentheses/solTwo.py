class Solution(object):
    def generateParenthesis(self, n):
        result = []
        def helper(st,stack,count,n):
            if stack == 0 and count == n:
                result.append(st)

            if count < n:
                helper(st+"(",stack+1,count+1,n)
            if stack > 0:
                helper(st+")",stack-1,count,n)

        
        helper("(",1,1,n)
        return result


s = Solution()
print(s.generateParenthesis(8))