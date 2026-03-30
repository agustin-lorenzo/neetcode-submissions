class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = [] # [startidx, height]

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                previ, prevh = stack.pop()
                largest = max(largest, prevh * (i - previ))
                start = previ
            stack.append([start, h])
        
        while stack:
            i, h = stack.pop()
            largest = max(largest, h * (len(heights) - i))
        
        return largest