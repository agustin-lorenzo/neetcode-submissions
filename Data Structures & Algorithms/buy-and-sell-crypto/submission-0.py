class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left, right = 0, 1 # left: buy, right: sell

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        
        return maxProfit

