class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        sums = []
        
        
        for i in range(len(nums)):
            if nums[i-1] != nums[i] or i == 0:
                self.threeSumHelper(nums, i, sums)          
        return sums
        
    def threeSumHelper(self, nums, start, sums):
        
        low = start + 1
        high = len(nums) - 1
        while low < high:
            result = nums[start] + nums[low] + nums[high] 
            if result == 0:
                sums.append([nums[start], nums[low], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
            elif result > 0:
                high -= 1
            elif result < 0:
                low += 1


print(Solution().threeSum([-1,0,1,2,-1,-4]))