class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])

        def capture(r, c):
            if (r not in range(R) or
                c not in range(C) or
                board[r][c] != "O"):
                return 
                
            board[r][c] = "#"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. capture UNsurrounded regions (O -> #)
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O" and r in [0, R - 1] or c in [0, C - 1]:
                    capture(r, c)

        # 2. capture surrounded regions (O -> X)
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. uncapture unsurrounded regions (# -> O)
        for r in range(R):
            for c in range(C):
                if board[r][c] == "#":
                    board[r][c] = "O"