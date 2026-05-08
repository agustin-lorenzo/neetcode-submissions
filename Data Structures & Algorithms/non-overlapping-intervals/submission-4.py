class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result = 0

        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prevEnd:
                prevEnd = min(end, prevEnd)
                result += 1
            else:
                prevEnd = end
        
        return result