class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        l = 0
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            result = max(result, profit)
            
            if prices[l] >= prices[r]:
                l = r
        
        return result