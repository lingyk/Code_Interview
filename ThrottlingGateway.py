
class solution(object):
    def Throttling(self, nums):
        ans = 0
        for i in range (len(nums)):
            if (i > 2 and nums[i] == nums[i-3]):
                ans+=1
            elif i>19 and (nums[i] - nums[i-20])<10:
                ans+=1
            elif i>59 and (nums[i]-nums[i-60])<60:
                ans+=1
        return ans
print(solution().Throttling([1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7]))
