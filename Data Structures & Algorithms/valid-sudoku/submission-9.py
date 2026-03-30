class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, blocks = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
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