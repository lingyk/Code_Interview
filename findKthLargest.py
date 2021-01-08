import heapq

class Solution(object):
    def findKthLargest(self, nums, k):

        return sorted(nums)[len(nums)-k]

    def findKthLargest2(self, nums, k):

        return heapq.nlargest(k, nums)[-1]
print(Solution().findKthLargest([3,2,1,5,6,4], 2))
print(Solution().findKthLargest2([3,2,1,5,6,4], 2))