class Solution(object):

    def subarrayMaxMin(self, arr,k):
        
        minima = []
        for i in range (len(arr) - k + 1):
            subarray = []
            for j in range (k):
                subarray.append(arr[i+j])
        minima.append(min(subarray))
        return minima

#[1,2,3,4,5]
print(Solution().subarrayMaxMin([1,2,3,4,5],3))
