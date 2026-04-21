class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        largest = 0

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            largest = max(area, largest)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
        return largest