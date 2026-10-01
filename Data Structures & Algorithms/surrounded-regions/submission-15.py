class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])

        def dfs(r, c):
            if board[r][c] == "X":
                return             
            board[r][c] = "#"
            q = deque([(r, c)])

            while q:
                row, col = q.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (nr in range(R) and
                        nc in range(C) and
                        board[nr][nc] == "O"):

                        board[nr][nc] = "#"
                        q.append((nr, nc))
        
        for r in range(R):
            dfs(r, 0)
            dfs(r, C - 1)
        
        for c in range(C):
            dfs(0, c)
            dfs(R - 1, c)
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == "#":
                    board[r][c] = "O"
