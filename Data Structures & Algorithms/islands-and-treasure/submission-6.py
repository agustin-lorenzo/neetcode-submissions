class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # * multi-source BFS
        # * append all chests to a queue at the same time
        # * rewrite cells as encountered with distance from BFS

        R, C = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()

        # Identify chests
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))
        
        # Start BFS
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(R) and
                        nc in range(C) and
                        grid[nr][nc] != -1 and
                        (nr, nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr, nc))
            dist += 1