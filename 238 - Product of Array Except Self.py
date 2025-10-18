class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        output = [1] * n
        
        for i in range(1, n):
            output[i] = output[i-1] * nums[i-1]
        
        suffix_product = 1
        for i in range(n-1, -1, -1):
            output[i] = output[i] * suffix_product
            suffix_product = suffix_product * nums[i]
        
        return output

nums = [1, 2, 3, 4]
obj = Solution()
print(obj.productExceptSelf(nums))
