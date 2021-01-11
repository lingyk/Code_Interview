class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.stack1 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        while self.stack:
            self.stack1.append(self.stack.pop())
        self.stack.append(x)
        while self.stack1:
            self.stack.append(self.stack1.pop())
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        
        return not self.stack
