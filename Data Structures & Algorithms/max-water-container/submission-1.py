class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        def getArea(a, b):
            waterLevel = min(heights[a], heights[b])
            width = b - a
            return waterLevel * width

        start = 0
        end = len(heights) - 1
        maxArea = 0
        while start < end:
            currentArea = getArea(start, end)
            maxArea = max(currentArea, maxArea)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
                
        return maxArea
