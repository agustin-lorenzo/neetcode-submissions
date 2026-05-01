class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = collections.deque()
        fresh, rotten = 0, 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten += 1
                    q.append((r, c))
        
        minutes = 0
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(R) and
                        nc in range(C) and
                        grid[nr][nc] == 1):
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1
