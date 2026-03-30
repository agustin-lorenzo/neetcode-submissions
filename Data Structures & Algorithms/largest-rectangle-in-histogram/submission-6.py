class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = [] # [startidx, height]

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                previ, prevh = stack.pop()
                largest = max(largest, prevh * (i - previ))
                start = previ
            stack.append([start, h])
        
        for i, h in stack:
            largest = max(largest, h * (len(heights) - i))
        
        return largest