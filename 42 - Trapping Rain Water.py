class Solution:
    def trap(self, height):
        left, right = 0, len(height) - 1
        leftmax, rightmax, trappedwater = 0, 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    trappedwater += leftmax - height[left]
                left += 1
            else:
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    trappedwater += rightmax - height[right]
                right -= 1
        return trappedwater


height = [0,1,0,2,1,0,1,3,2,1,2,1]
height2 = [4,2,0,3,2,5]
a = Solution()
print(a.trap(height2))
