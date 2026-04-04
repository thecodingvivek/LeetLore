def countGoodNumbers(n):
    MOD = 10**9 + 7
    evencount = (n + 1)//2
    oddcount = n//2
    def pow(num,p):
        num = num % MOD
        if p == 0:
            return 1
        
        if p == 1:
            return num

        half = pow(num,p//2) % MOD
        if p%2 ==0:
            return half * half
        else:
            return half * half * num
        
    return (pow(5,evencount) * pow(4,oddcount) )%MOD

print(countGoodNumbers(4))