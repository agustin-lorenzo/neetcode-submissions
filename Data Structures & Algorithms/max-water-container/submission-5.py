class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0

        l, r = 0, len(heights) - 1

        while l < r:
            h = min(heights[l], heights[r])
            w = r - l # TODO: check 0-index
            area = w * h
            maximum = max(maximum, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maximum