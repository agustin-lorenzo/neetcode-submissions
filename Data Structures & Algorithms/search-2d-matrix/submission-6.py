class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. binary search to find correct row
        #       * return false if that row doesn't exist
        # 2. binary search on row's columns to find target
        #       * return false if not in row

        # edge case: target is completely out of bounds
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        # identify correct row
        R, C = len(matrix), len(matrix[0])

        top, bottom = 0, R - 1
        tRow = matrix[(top + bottom) // 2]
        while top <= bottom:
            mid = (top + bottom) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                tRow = matrix[mid]
                break
        
        l, r = 0, len(tRow) - 1
        while l <= r:
            mid = (l + r) // 2
            if target < tRow[mid]:
                r = mid - 1
            elif target > tRow[mid]:
                l = mid + 1
            else:
                return True
        
        return False