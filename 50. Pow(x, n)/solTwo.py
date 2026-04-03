def myPow(x, n):
    if n == 0:
        return 1

    if n == 1:
        return x

    if n<0:
        return 1/myPow(x,-n)
    
    half = myPow(x,n//2)

    if n%2 == 0:
        return half * half
    else:
        return half * half * x


print(myPow(10,2))