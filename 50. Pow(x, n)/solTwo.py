def myPow(x, n):
    temp = n
    def helper(i,var):
        if i == 0:
            return 1

        if i == 1:
            return x
       
        if i%2 == 0:
            half = helper(i//2,x)
            return half * half
        else:
            half = (helper(i//2,x))
            return half * half * x

    return helper(temp,x)

print(myPow(10,2))