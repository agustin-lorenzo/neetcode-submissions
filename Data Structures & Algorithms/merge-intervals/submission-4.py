class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        result.append(intervals[0])

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            prevStart, prevEnd = result[-1]

            if start <= prevEnd:
                mergeStart = min(start, prevStart)
                mergeEnd = max(end, prevEnd)
                result[-1] = [mergeStart, mergeEnd]
            
            else:
                result.append([start, end])
        
        return result

