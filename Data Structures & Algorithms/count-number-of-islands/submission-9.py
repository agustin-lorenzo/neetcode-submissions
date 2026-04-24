class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        board = grid
        R, C = len(board), len(board[0])
        islands = 0
        visited = set()
        
        def dfs(r, c):
            if (r not in range(R) or
                c not in range(C) or
                board[r][c] != "1" or
                (r, c) in visited):
                return

            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(R):
            for c in range(C):
                if board[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        return islands