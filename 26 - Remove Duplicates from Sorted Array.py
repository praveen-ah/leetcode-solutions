class Solution:
    def removeDuplicates(self, nums):
        left = 0
        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
        print(nums) 
        print(left + 1)

nums = [0,0,1,1,1,2,2,3,3,4]
nums2 = [1,1,2]
nums3 = [1,2]
obj = Solution()
obj.removeDuplicates(nums3)