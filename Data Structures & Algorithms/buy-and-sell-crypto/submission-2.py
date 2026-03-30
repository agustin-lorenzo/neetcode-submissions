class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        left, right = 0, 1
        maxProfit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:    
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            
            right += 1
        
        return maxProfit

