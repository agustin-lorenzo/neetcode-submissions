class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        fresh = 0
        q = collections.deque()
        visited = set()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(R) and
                        nc in range(C) and
                        (nr, nc) not in visited and
                        grid[nr][nc] == 1):
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1