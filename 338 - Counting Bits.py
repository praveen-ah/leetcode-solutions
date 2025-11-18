class Solution:
    def countBits(self, n):
        # arr = []
        # for i in range(0, n+1):
        #     cnt = bin(i).count('1')
        #     arr.append(cnt)
        # return arr
        arr = [0] * (n+1)
        for i in range(1, n+1):
            arr[i] = arr[i // 2] + i % 2
        return arr

n = 2
n2 = 5
obj = Solution()
print(obj.countBits(n2))
