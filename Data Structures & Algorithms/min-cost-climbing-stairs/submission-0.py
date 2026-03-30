class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def search(i):
            if i == len(cost):
                return 0
            if i == len(cost) - 1:
                return cost[-1]
            
            return cost[i] + min(search(i + 1), search(i + 2))

        return min(search(0), search(1))