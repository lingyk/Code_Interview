import collections

class Solution(object):
    def topKfrequent(self, nums, k):
        valid_k = 0
        frequent_ele = []
        array = collections.Counter(nums).items()
        sorted(array, key=lambda x:x[1], reverse=True)
        for x, y in array:
            frequent_ele.append(x)
        return frequent_ele[:k]
            
print(Solution().topKfrequent([1,1,1,2,2,3], 2))