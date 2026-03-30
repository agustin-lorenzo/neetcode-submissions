class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])

        # 1. (DFS) Capture unsurrounded regions (O -> T)
        def capture(r, c):
            if (min(r, c) < 0 or r == R or c == C or
                board[r][c] != 'O'):
                return
            board[r][c] = 'T'
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(R):
            for c in range(C):
                if (board[r][c] == 'O' and
                    (r in [0, R-1] or
                    c in [0, C-1])):
                    capture(r, c)

        # 2. Capture surrounded regions (O -> X)
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'T':
                    board[r][c] = 'O'