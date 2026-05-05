class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i >= len(word):
                return True
                
            if (r in range(R) and
                c in range(C) and
                (r, c) not in visited and
                board[r][c] == word[i]):

                visited.add((r, c))
                result = (dfs(r + 1, c, i + 1) or
                        dfs(r - 1, c, i + 1) or
                        dfs(r, c + 1, i + 1) or
                        dfs(r, c - 1, i + 1))
                visited.remove((r, c))
                return result
            
            return False

        for r in range(R):
            for c in range(C):
                if dfs(r, c, 0):
                    return True
        return False