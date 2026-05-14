class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])

        # 1. transpose
        for r in range(R):
            for c in range(r + 1, C):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            
        # 2. reverse
        for row in matrix:
            l, r = 0, C - 1
            while l < r:
                row[l], row[r] = row[r], row[l]
                l += 1
                r -= 1