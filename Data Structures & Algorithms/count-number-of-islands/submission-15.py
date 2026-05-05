class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])

        def bfs(r, c):
            grid[r][c] = "0"
            q = collections.deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(R) and
                        nc in range(C) and
                        grid[nr][nc] == "1"):
                        grid[nr][nc] = "0"
                        q.append((nr, nc))
        
        islands = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        
        return islands