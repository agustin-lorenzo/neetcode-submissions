class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def dfs(r, c):
            visited.add((r, c))
            q = collections.deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (
                        nr in range(R) and
                        nc in range(C) and
                        (nr, nc) not in visited and
                        grid[nr][nc] == "1"
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(R):
            for c in range(C):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands