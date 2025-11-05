class Solution:
    def maxProfit(self, prices):
        total_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total_profit += prices[i] - prices[i-1]
        return total_profit
        

prices = [7,1,5,3,6,4]
prices2 = [1,2,3,4,5]
obj = Solution()
print(obj.maxProfit(prices2))