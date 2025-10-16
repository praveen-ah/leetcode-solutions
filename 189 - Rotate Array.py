class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        def reverse(start, end):
            while (start < end):
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
        return nums

        # k = k % len(nums)
        # nums[:k], nums[k:] = nums[-k:], nums[:-k]
        # return nums


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
obj = Solution()
print(obj.rotate(nums, k))
