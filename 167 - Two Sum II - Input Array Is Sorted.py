class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            res = numbers[left] + numbers[right]
            if res == target:
                return [left+1, right+1]
            elif res > target:
                right -= 1
            else:
                left += 1
        return []


obj = Solution()
numbers = [2,7,11,15]
target = 18
print(obj.twoSum(numbers, target))