class Solution:
    def firstMissingPositive(self, nums):
        nums.sort()
        missing_num = 1
        for i in nums:
            if i == missing_num:
                missing_num += 1
            elif i > missing_num:
                break
        return missing_num


nums = [1, 2, 0]
nums2 = [3, 4, -1, 1]
nums3 = [7, 8, 9, 11, 12]
nums4 = [1]
obj = Solution()
print(obj.firstMissingPositive(nums4))
