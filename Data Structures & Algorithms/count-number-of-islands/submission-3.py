class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.pop()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(R) and
                        nc in range(C) and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visited):

                        visited.add((nr, nc))
                        q.append((nr, nc))


        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        return islands