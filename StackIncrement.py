class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.nums = []
        self.maxSize = maxSize
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.nums) < self.maxSize:
            return self.nums.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.nums) > 0:
            return self.nums.pop()
        else:
            return -1

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if len(self.nums) < k:
            for i in range(len(self.nums)):
                self.nums[i] = self.nums[i] + val
        else:
            for i in range(k):
                self.nums[i] = self.nums[i] + val

array = [2,3,4,5,6]
print(array.pop())