class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        numFresh = 0        

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    numFresh += 1
        
        minutes = 0
        while q and numFresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(R) and
                        nc in range(C) and
                        grid[nr][nc] == 1):

                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        numFresh -= 1

            minutes += 1
        
        return minutes if numFresh == 0 else -1
