class Solution:
    def increasingTriplet(self, nums):
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


nums = [1, 2, 3, 4, 5]
nums2 = [5, 4, 3, 2, 1]
nums3 = [2, 1, 5, 0, 4, 6]
nums4 = [20,100,10,12,5,13]
obj = Solution()
print(obj.increasingTriplet(nums4))
