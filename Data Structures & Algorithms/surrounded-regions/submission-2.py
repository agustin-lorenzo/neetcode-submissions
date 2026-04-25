class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        q = collections.deque()
        visited = set()
        
        for c in range(C):
            if board[0][c] == "O":
                q.append((0, c))
            if board[R - 1][c] == "O":
                q.append((R - 1, c))
        
        for r in range(R):
            if board[r][0] == "O":
                q.append((r, 0))
            if board[r][C - 1] == "O":
                q.append((r, C - 1))
        
        while q:
            r, c = q.popleft()
            board[r][c] = "#"

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr in range(R) and
                    nc in range(C) and
                    (nr, nc) not in visited and
                    board[nr][nc] == "O"):
                    visited.add((nr, nc))
                    q.append((nr, nc))
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(R):
            for c in range(C):
                if board[r][c] == "#":
                    board[r][c] = "O"