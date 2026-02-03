class Solution:
    def maxArea(self, height):
        res = float('-inf')
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                cap = height[left] * (right - left)
                res = max(cap, res)
                left += 1
            else:
                cap = height[right] * (right - left)
                res = max(cap, res)
                right -= 1
        return res


height = [1,8,6,2,5,4,8,3,7]
height2 = [1,1]
obj = Solution()
print(obj.maxArea(height2))