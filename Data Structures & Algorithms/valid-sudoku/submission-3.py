class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = {}

        for r in range(9):
            for c in range(9):
                current = board[r][c]
                if current == ".":
                    continue
                    
                if current in rows[r] or current in cols[c]:
                    return False
                
                rows[r].add(current)
                cols[c].add(current)

                if (r // 3, c // 3) not in blocks:
                    blocks[(r // 3, c //3)] = set()
                if current in blocks[(r // 3, c // 3)]:
                    return False
                blocks[(r // 3, c // 3)].add(current)
        
        return True