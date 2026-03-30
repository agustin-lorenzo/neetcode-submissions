class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = defaultdict(set)

        for r in range(9):
            for c in range(9):
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
