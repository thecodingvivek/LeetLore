class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mini = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.mini = val

        if val<self.mini:
            self.mini = val
        
        self.stack.append(val)

        

    def calcMin(self):
        if not self.stack:
            return None
        return min(self.stack)

    def pop(self):
        """
        :rtype: None
        """
        p = self.stack.pop()
        if p == self.mini:
            self.mini = self.calcMin()
        return p


        

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()