class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        
        for start, end in intervals[1:]:
            if start <= result[-1][1]:
                mergeStart = min(result[-1][0], start)
                mergeEnd = max(result[-1][1], end)
                result[-1] = [mergeStart, mergeEnd]
            else:
                result.append([start, end])
        
        return result