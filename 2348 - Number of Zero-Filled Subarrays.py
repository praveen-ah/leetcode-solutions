class Solution:
    def zeroFilledSubarray(self, nums):
        cnt = 0
        zeroSeqLen = 0

        for num in nums:
            if num == 0:
                zeroSeqLen += 1
                cnt += zeroSeqLen
            else:
                zeroSeqLen = 0
        return cnt
            

nums = [1,3,0,0,2,0,0,4]
nums2 = [0,0,0,2,0,0]
nums3 = [2,10,2019]
obj = Solution()
print(obj.zeroFilledSubarray(nums2))

