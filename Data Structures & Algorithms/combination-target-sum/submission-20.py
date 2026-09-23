class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        combo = []

        def dfs(i, total):
            if total == target:
                result.append(combo.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            combo.append(nums[i])
            dfs(i, total + nums[i])

            combo.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i + 1
            dfs(i + 1, total)

        dfs(0, 0)
        return result
