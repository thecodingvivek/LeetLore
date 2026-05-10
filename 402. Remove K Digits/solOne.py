class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n=0
        stack=[]
        s=0

        for i in num:
            while stack and k>0 and stack[-1] > i:
                    stack.pop()
                    k-=1
            stack.append(i)

        while k>0:
            stack.pop()
            k-=1
        
        result = ''.join(stack).lstrip('0')
        return result if result else "0"






s=Solution()
print(s.removeKdigits("1432219",3))