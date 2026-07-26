class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        def dfs(r, c):
            if (r not in range(R) or
                c not in range(C) or
                (r, c) in visited or
                grid[r][c] != 1):
                return 0
            
            visited.add((r, c))
            return 1 + (dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))


        for r in range(R):
            for c in range(C):
                if (r, c) not in visited and grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea