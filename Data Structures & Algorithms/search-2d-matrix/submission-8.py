class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])

        top, bot = 0, R - 1
        row = None
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                row = mid
                break

        if row == None:
            return False

        row = matrix[(top + bot) // 2]
        l, r = 0, C - 1
        while l <= r:
            mid = (l + r) // 2
            if target > row[mid]:
                l = mid + 1
            elif target < row[mid]:
                r = mid - 1
            else:
                return True

        return False