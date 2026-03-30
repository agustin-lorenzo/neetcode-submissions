class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R, C = len(board), len(board[0])
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)

        for r in range(R):
            for c in range(C):
                n = board[r][c]
                if n == ".":
                    continue
                
                if (n in rows[r] or
                    n in cols[c] or
                    n in blocks[(r // 3, c // 3)]):
                    return False
                
                rows[r].add(n)
                cols[c].add(n)
                blocks[(r // 3, c //3)].add(n)
        
        return True