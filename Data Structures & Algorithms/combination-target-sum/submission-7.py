class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        combo = []
        def dfs(i, total):
            if i >= len(nums):
                if total == target:
                    result.append(combo.copy())
                return
            
            if nums[i] + total <= target:
                combo.append(nums[i])
                dfs(i, total + nums[i])
                combo.pop()
            
            dfs(i + 1, total)

        dfs(0, 0)
        return result