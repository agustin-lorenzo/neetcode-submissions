class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l = 0

        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            best = max(best, profit)
            if prices[r] < prices[l]:
                l = r
        
        return best