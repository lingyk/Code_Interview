class Solution(object):
    def nonDupliNum(self, nums):
        array = {}
        for item in nums:
            array[item] = array.get(item, 0) + 1
        for key, value in array.items():
            if value == 1:
                return key


print(Solution().nonDupliNum([4,3,4,1,3,5]))