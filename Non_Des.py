class Solution(object):
    def checkPossibility(self, nums):
        invalid_index = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if invalid_index != -1:

                    return False
                invalid_index = i
        if invalid_index == -1:
            return True
        if invalid_index == 0:
            return True 
        if nums[invalid_index] <= nums[invalid_index+2]:
            return True
        if invalid_index == len(nums) - 2:
            return True
        if nums[invalid_index + 1] >= nums[invalid_index - 1]:
            return True
        return False
    
print(Solution().checkPossibility([4,1,2]))
print(Solution().checkPossibility([3,2,4,1]))