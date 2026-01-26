class Solution:
    # def merge(self, nums1, m, nums2, n):
    #     for i in range(m):
    #         nums1[i+m] = nums2[i]
    #     nums1.sort()
    #     return nums1
    def merge(self, nums1, m, nums2, n):
        left = m - 1
        right = n - 1
        pos = (m+n) - 1
        while right >= 0:
            if left >= 0 and nums1[left] > nums2[right]:
                nums1[pos] = nums1[left]
                left -= 1
            else:
                nums1[pos] = nums2[right]
                right -= 1
            pos -= 1
        return nums1


obj = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(obj.merge(nums1, m, nums2, n))
