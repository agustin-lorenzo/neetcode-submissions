class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        result = []

        combo = []
        def backtrack(i, total):
            if total == target:
                result.append(combo.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            combo.append(nums[i])
            backtrack(i + 1, nums[i] + total)
            combo.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, total)
        
        backtrack(0, 0)
        return result