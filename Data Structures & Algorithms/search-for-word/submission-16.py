class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        visited = set()

        def dfs(i, r, c):
            if i == len(word):
                return True
            
            if (r not in range(R) or
                c not in range(C) or
                (r, c) in visited or
                board[r][c] != word[i]):
                return False
            
            visited.add((r, c))
            result = (dfs(i + 1, r + 1, c) or
                      dfs(i + 1, r - 1, c) or
                      dfs(i + 1, r, c + 1) or
                      dfs(i + 1, r, c - 1)) 
            visited.remove((r, c))
            return result
        
        for r in range(R):
            for c in range(C):
                if dfs(0, r, c):
                    return True
        return False