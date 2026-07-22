class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            start, end = intervals[i]
            if newInterval[1] < start:
                result.append(newInterval)
                return result + intervals[i:]
            
            elif newInterval [0] > end:
                result.append(intervals[i])
            
            else:
                newStart = min(start, newInterval[0])
                newEnd = max(end, newInterval[1])
                newInterval = [newStart, newEnd]
            
        result.append(newInterval)
        return result