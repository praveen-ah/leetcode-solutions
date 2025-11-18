class Solution:
    def rangeBitwiseAnd(self, left, right):
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift



left = 5
right = 7
obj = Solution()
print(obj.rangeBitwiseAnd(left, right))
