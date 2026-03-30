class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        l, r = 0, len(heights) - 1
        while l < r:
            w, h = r - l, min(heights[l], heights[r])
            area = w * h
            maxWater = max(maxWater, area)
            
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return maxWater