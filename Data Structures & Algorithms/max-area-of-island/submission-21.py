class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = set()
        result = 0

        def dfs(r, c):
            if (r not in range(R) or
                c not in range(C) or
                (r, c) in visited or
                grid[r][c] != 1):
                return 0
            
            visited.add((r, c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        for r in range(R):
            for c in range(C):
                result = max(result, dfs(r, c))
        return result