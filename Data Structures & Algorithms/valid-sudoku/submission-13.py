class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R, C = len(board), len(board[0])
        rows = {r: set() for r in range(R)}
        cols = {c: set() for c in range(C)}
        blocks = {(r, c): set() for r in range(3) for c in range(3)}

        for r in range(R):
            for c in range(C):
                curr = board[r][c]
                if curr == ".":
                    continue
                
                if (curr in rows[r] or
                    curr in cols[c] or
                    curr in blocks[(r // 3, c // 3)]):
                    return False

                rows[r].add(curr)
                cols[c].add(curr)
                blocks[(r // 3, c // 3)].add(curr)
        
        return True
