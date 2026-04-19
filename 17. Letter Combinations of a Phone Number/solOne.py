class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result=[]
        def helper(i,out,n):
            if len(out)==n:
                result.append(out)
                return

            if i >= len(digits):
                return
            poss = letters[digits[i]]

            for j in poss:
                helper(i+1,out+j,n)

            
        helper(0,"",len(digits))
        print(result)

s= Solution()
s.letterCombinations("23")