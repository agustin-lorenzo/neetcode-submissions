class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        l = 0

        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            result = max(profit, result)

            if prices[r] < prices[l]:
                l = r
        
        return result