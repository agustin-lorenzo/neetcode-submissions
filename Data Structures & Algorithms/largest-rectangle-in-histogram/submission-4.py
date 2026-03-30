class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # [i, h]

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                prevI, prevH = stack.pop()
                start = prevI
                area = (i - prevI) * prevH
                maxArea = max(area, maxArea)            

            stack.append([start, h])
        
        for i, h in stack: # STACK MIGHT NOT BE EMPTY AFTER ITERATING
                           # currently outside of heights, so to get width,
                           # you take the lengths and subtract i from it
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea

        
