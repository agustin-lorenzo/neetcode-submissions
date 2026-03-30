class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        
        def dfs(i, current, total):
            if total == target:
                result.append(current.copy())
                return

            if total > target or i == len(candidates):
                return
            
            # include candidates[i]
            current.append(candidates[i])
            dfs(i + 1, current, total + candidates[i])
            current.pop()
            # skip candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, current, total)

        dfs(0, [], 0)
        return result