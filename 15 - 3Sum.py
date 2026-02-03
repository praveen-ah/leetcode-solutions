class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                left, right = i + 1, len(nums) - 1
                while left < right:
                    s = nums[i] + nums[left] + nums[right]
                    if s == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif s < 0:
                        left += 1
                    elif s > 0:
                        right -= 1
        return res


nums = [-1,0,1,2,-1,-4]
nums2 = [0,1,1]
nums3 = [-100,-70,-60,110,120,130,160]
obj = Solution()
print(obj.threeSum(nums3))