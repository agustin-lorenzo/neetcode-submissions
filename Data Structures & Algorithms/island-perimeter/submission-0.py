class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        perimiter = 0
        visited = set()

        def dfs(r, c):
            if (r, c) in visited:
                return 0

            if (r not in range(R) or
                c not in range(C) or
                grid[r][c] == 0):
                return 1
            
            visited.add((r, c))
            result = (dfs(r + 1, c) + 
                      dfs(r - 1, c) +
                      dfs(r, c + 1) +
                      dfs(r, c - 1))
            return result
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    return dfs(r, c)
        return perimiter