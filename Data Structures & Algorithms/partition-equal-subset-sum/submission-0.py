from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        @cache
        def dfs(i, total):
            if total * 2 == s:
                return True
            
            if i == len(nums):
                return False
            
            skip = dfs(i + 1, total)
            keep = dfs(i + 1, total + nums[i])
            return skip or keep
        
        return dfs(0, 0)