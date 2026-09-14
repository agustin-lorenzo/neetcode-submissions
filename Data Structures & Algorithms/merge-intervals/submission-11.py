class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= result[-1][1]:
                newStart = min(start, result[-1][0])
                newEnd = max(end, result[-1][1])
                result[-1] = [newStart, newEnd]
            else:
                result.append([start, end])
        
        return result
