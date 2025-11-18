class Solution:
    def singleNumber(self, nums):
        xor = 0
        for num in nums:
            xor ^= num
        
        diff = xor & -xor

        res = [0, 0]
        for num in nums:
            if num & diff == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res


nums = [1, 2, 1, 3, 2, 5]
obj = Solution()
print(obj.singleNumber(nums))
