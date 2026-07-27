from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        time = 0
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(R) and
                        nc in range(C) and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            
            time += 1
        
        return time if not fresh else -1