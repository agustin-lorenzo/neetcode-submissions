class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()

        def addRoom(r, c):
            if (r not in range(R) or
                c not in range(C) or
                (r, c) in visited or
                grid[r][c] == -1):
                return
            visited.add((r, c))
            q.append((r, c))

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)

            dist += 1