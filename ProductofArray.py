class Solution(object):
    def productArray(self, nums):
        result = [1 for _ in range(len(nums))]
        
        product = 1
        for i in range(len(nums)-2, -1, -1):
            product *= nums[i+1]
            result[i] = product
        print(result)
        product = 1
        for i in range (1, len(nums)): #1, 2, 3
            
            product *= nums[i-1] #0,1,2
            print(product)
            result[i] *= product
        return result 
print(Solution().productArray([1,2,3,4]))