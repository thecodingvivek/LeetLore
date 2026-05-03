class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in asteroids:
            app = i
            while stack and stack[-1] > 0 and i < 0:
                if abs(i) > abs(stack[-1]):
                    stack.pop()
                elif abs(i) < abs(stack[-1]):
                    app=None
                    break
                elif abs(i) == abs(stack[-1]):
                    stack.pop()
                    app=None
                    break
                
            if app:
                stack.append(i)
        
        return stack

        

s=Solution()
print(s.asteroidCollision(asteroids = [10,2,-5]))
