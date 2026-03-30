class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def dfs(r, c):
            if (r in range(R) and
                c in range(C) and
                (r, c) not in visited and
                grid[r][c] == "1"):

                visited.add((r, c))
                dfs(r + 1, c)
                dfs(r, c + 1)
                dfs(r - 1, c)
                dfs(r, c - 1)


        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        return islands