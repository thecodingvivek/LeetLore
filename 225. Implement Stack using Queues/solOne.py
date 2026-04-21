from collections import deque
class MyStack(object):


    def __init__(self):
        self.queue = deque()

        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        l = len(self.queue)
        self.queue.append(x)
        for i in range(l):
            temp = self.queue.popleft()
            self.queue.append(temp)
        



        

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        return self.queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        
        return not len(self.queue)


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(10)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2,param_3,param_4)