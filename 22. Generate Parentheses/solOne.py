n = 3
n = 3


def generateParenthesis(n):
    result = []

    def helper(n,close,openn,string):
        if close + openn == 2 * n:
            result.append(string)
            return 
        
        if openn < n:
            helper(n,close,openn+1,string+"(")

        if close < openn:
            helper(n,close+1,openn,string+")")

    helper(n,0,0,"")
    print(result)
            

    
generateParenthesis(n)