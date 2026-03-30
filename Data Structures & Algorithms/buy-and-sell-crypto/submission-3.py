class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        if len(prices) == 1:
            return result
        
        l, r = 0, 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            result = max(result, profit)

            if prices[r] < prices[l]:
                l = r
            r += 1

        return result