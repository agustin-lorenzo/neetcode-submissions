class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        visited = set()

        q = collections.deque()
        for r in range(R):
            for c in range(C):
                if (r, c) not in visited and grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))
        
        distance = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = distance
                
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(R) and
                        nc in range(C) and
                        (nr, nc) not in visited and
                        grid[nr][nc] != -1):

                        q.append((nr, nc))
                        visited.add((nr, nc))


            distance += 1
