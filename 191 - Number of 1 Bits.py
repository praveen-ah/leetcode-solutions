class Solution:
    def hammingWeight(self, n):
        a = format(n, 'b')
        return str(a).count('1')
        # return bin(n).count('1')



n = 11
obj = Solution()
print(obj.hammingWeight(n))