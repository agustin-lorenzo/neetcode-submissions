class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        
        for r in range(R):
            for c in range(C):
                if r in rows or c in cols:
                    matrix[r][c] = 0
        