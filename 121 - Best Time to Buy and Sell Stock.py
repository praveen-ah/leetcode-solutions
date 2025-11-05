class Solution:
    def maxProfit(self, prices):
        left = prices[0]
        profit = 0
        for right in prices[1:]:
            if left > right:
                left = right
            profit = max(profit, right-left)
        return profit


prices = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]
prices3 = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
obj = Solution()
print(obj.maxProfit(prices))
