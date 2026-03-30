class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(i, current):
            if sum(current) == target:
                result.append(current.copy())
                return

            if i >= len(candidates):
                return
            
            if sum(current) + candidates[i] <= target:
                current.append(candidates[i])
                backtrack(i + 1, current)
                current.pop()
            
            j = i
            while j + 1 < len(candidates) and candidates[j + 1] == candidates[i]:
                j += 1
            backtrack(j + 1, current)

        backtrack(0, [])
        return result