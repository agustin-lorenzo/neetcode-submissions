class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            start, end = intervals[i]

            if newInterval[1] < start:
                result.append(newInterval)
                return result + intervals[i:]
            
            elif newInterval[0] > end:
                result.append([start, end])
            
            else:
                mergeStart = min(start, newInterval[0])
                mergeEnd = max(end, newInterval[1])
                newInterval = [mergeStart, mergeEnd]
            
        result.append(newInterval)
        return result
