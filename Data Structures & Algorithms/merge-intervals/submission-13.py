class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            prevStart, prevEnd = result[-1]

            if start <= prevEnd:
                newStart = min(start, prevStart)
                newEnd = max(end, prevEnd)
                result[-1] = [newStart, newEnd]
            else:
                result.append([start, end])
        
        return result