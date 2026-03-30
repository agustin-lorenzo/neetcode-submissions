class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        blocks = defaultdict(set)

        R, C, = len(board), len(board[0])

        for r in range(R):
            for c in range(C):
                current = board[r][c]
                if current == ".":
                    continue
                
                if (current in rows[r] or
                    current in columns[c] or
                    current in blocks[(r // 3, c // 3)]
                ):
                    return False
                
                rows[r].add(current)
                columns[c].add(current)
                blocks[(r // 3, c // 3)].add(current)
        
        return True