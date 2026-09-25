class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for i in intervals[1:]:
            start, end = i[0], i[1]
            prevStart, prevEnd = result[-1][0], result[-1][1]

            if start <= prevEnd:
                newStart = min(start, prevStart)
                newEnd = max(end, prevEnd)
                result[-1] = [newStart, newEnd]

            else:
                result.append([start, end])
        
        return result