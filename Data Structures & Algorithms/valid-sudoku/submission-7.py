class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                current = board[r][c]
                if current == ".":
                    continue
                
                
                if (current in rows[r] or
                    current in cols[c] or
                    current in blocks[(r // 3, c // 3)]):
                    return False
                
                rows[r].add(current)
                cols[c].add(current)
                blocks[(r // 3, c // 3)].add(current)
        
        return True