class Solution(object):
    def myAtoi(self, s):
        final = ""
        sign = 1
        i=0
        lenn = len(s)

        while i<lenn and s[i] == " ":
            i+=1
        
        if i<lenn and s[i] == "-":
            sign = -1
            i+=1
        elif i<lenn and s[i] == "+":
            i+=1


        num = 0
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        while i<lenn and s[i].isdigit():
            digi = int(s[i])
            if num > (MAX_INT - digi)//10:
                if sign == -1:
                    return MIN_INT
                else:
                    return MAX_INT
            
            num = (num * 10) + digi
            i+=1
        
        return sign * num

        


s = Solution()
print(s.myAtoi("   0197"))