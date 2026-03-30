class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0

        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            maxProfit = max(profit, maxProfit)

            if prices[r] < prices[l]:
                l = r
        
        return maxProfit