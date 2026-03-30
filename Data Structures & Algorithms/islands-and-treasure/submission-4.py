class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(R) and
                        nc in range(C) and
                        (nr, nc) not in visited and
                        grid[nr][nc] != -1):

                        q.append((nr, nc))
                        visited.add((nr, nc))

            distance += 1