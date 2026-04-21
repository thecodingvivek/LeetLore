

class MyQueue(object):

    def __init__(self):
        self.os = []
        self.ss = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.os.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.ss.pop()
        
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.ss:
            while self.os:
                self.ss.append(self.os.pop())
        return self.ss[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not len(self.os) and not len(self.ss)
        