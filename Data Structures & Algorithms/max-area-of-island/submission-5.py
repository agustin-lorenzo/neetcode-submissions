class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            area = 1

            while q:
                row, col = q.pop()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(R) and
                        nc in range(C) and
                        (nr, nc) not in visited and
                        grid[nr][nc] == 1):
                        area += 1
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return area

        for r in range(R):
            for c in range(C):
                if (r, c) not in visited and grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
        return maxArea