class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        maxArea = 0
        rows, cols = len(grid), len(grid[0])    
        visited = set() # (r, c)
        
        def bfs(r, c):
            islandSize = 1 # count first square (r, c)
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    if (nr in range(rows) and 
                        nc in range(cols) and
                        (nr, nc) not in visited and
                        grid[nr][nc] == 1):

                        q.append((nr, nc))
                        visited.add((nr, nc))
                        islandSize += 1 # current square (nr, nc)

            return islandSize


    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
        
        return maxArea