class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def dfs(i, total):
            if (i, total) in cache:
                return cache[(i, total)]
            
            if i == len(nums):
                if total == target:
                    return 1
                return 0
            
            result = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            cache[(i, total)] = result
            return result
        
        return dfs(0, 0)