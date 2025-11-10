class Solution:
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res = res ^ num
        return res

nums = [2,2,1]
nums2 = [4,1,2,1,2]
nums3 = [1]
obj = Solution()
print(obj.singleNumber(nums))