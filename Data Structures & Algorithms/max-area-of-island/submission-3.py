class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        def dfs(r, c):
            if (r not in range(R) or c not in range(C) or
                grid[r][c] != 1 or
                (r, c) in visited):
                return 0
                
            visited.add((r, c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r, c) not in visited:
                    currentArea = dfs(r, c)
                    maxArea = max(maxArea, currentArea)
        return maxArea