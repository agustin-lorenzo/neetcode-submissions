class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        l = 0
        for r in range(len(prices)):
            result = max(result, (prices[r] - prices[l]))
            if prices[r] < prices[l]:
                l = r
        
        return result