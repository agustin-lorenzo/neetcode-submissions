class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i:[] for i in range(9)}
        cols = {i:[] for i in range(9)}
        blocks = {} # (r, c) 0 <= r, c <= 2: 

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r]:
                    return False
                if val in cols[c]:
                    return False

                blockR = r // 3
                blockC = c // 3
                if (blockR, blockC) not in blocks:
                    blocks[(blockR, blockC)] = []
                if val in blocks[(blockR, blockC)]:
                    return False
                
                rows[r].append(val)
                cols[c].append(val)                
                blocks[(blockR, blockC)].append(val)
        
        return True