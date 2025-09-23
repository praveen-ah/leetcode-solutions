from collections import Counter


class Solution:
    def majorityElement(self, nums):
        cnt_nums = Counter(nums)
        max_cnt = len(nums) // 2
        for num, cnt in cnt_nums.items():
            if cnt > max_cnt:
                return num


nums = [2, 2, 1, 1, 1, 2, 2]
obj = Solution()
print(obj.majorityElement(nums))
