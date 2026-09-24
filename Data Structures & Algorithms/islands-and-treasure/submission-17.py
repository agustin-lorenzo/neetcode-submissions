from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        q = deque()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        dist = 0
        while q:
            dist += 1
            for i in range(len(q)):
                r, c = q.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(R) and
                        nc in range(C) and
                        grid[nr][nc] == 2147483647):

                        grid[nr][nc] = dist
                        q.append((nr, nc))