class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        row = -1
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                row = mid
                break
        if row == -1:
            return False
        
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
        return False
            