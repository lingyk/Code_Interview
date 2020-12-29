class Solution(object):
    def permute(self, nums, start=0):
        if start == len(nums) - 1:
            return [nums[:]]
        result = []
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            result += self.permute(nums, start+1)
            nums[i], nums[start] = nums[start], nums[i]
        return result

print(Solution().permute([1,2,3]))
 