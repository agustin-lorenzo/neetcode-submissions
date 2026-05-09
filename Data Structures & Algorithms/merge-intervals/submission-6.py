class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start <= prevEnd:
                result[-1][1] = max(prevEnd, end)
                prevEnd = max(prevEnd, end)
            else:
                result.append([start, end])
                prevEnd = end
        
        return result