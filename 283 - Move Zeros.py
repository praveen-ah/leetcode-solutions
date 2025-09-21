class Solution:
    def moveZeroes(self, nums):
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums


obj = Solution()
nums = [0, 1, 0, 3, 12]
nums2 = [1, 0, 1]
print(obj.moveZeroes(nums2))
