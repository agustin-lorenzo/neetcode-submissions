class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l = 0
        for r in range(len(prices)):
            best = max(best, prices[r] - prices[l])
            if prices[r] <= prices[l]:
                l = r
        return best