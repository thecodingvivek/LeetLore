class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        target=[]
        def helper(curr,stack,rem):
            if rem == 0 and len(stack)==k:
                target.append(stack)
                return
            if rem<0 or curr>8:
                return



            stack.append(curr+1)
            helper(curr+1,list(stack),rem-(curr+1))
            stack.pop()
            helper(curr+1,list(stack),rem)

        helper(0,[],n)
        print(target)


s = Solution()
s.combinationSum3(4,1)
