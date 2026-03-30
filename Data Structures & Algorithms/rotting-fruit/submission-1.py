class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (min(nr, nc) < 0 or
                        nr == R or
                        nc == C or
                        grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    q.append([nr, nc])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
        
        