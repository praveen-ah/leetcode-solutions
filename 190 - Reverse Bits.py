class Solution:
    def reverseBits(self, n):
        result = 0
        for _ in range(32):
            last = n & 1
            result = (result << 1) | last
            n >>= 1
        return result

n = 43261596
obj = Solution()
print(obj.reverseBits(n))