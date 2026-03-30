class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(i, r, c):
            if board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            
            ch = board[r][c]
            board[r][c] = '#'
            
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if (nr >= 0 and nr < len(board)
                and nc >= 0 and nc < len(board[0])
                and board[nr][nc] == word[i + 1]):
                    if backtrack(i + 1, nr, nc):
                        return True

            board[r][c] = ch
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and backtrack(0, r, c):
                    return True
        
        return False