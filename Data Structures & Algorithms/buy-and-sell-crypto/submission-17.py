class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices) - 1
        result = 0

        l = 0
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            result = max(result, profit)

            if prices[r] < prices[l]:
                l = r
        
        return result