class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        l, r = 0, len(heights) - 1
        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            water = w * h
            maxWater = max(maxWater, water)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater