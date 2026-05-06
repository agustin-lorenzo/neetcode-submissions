class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            start, end = intervals[i]
            if start > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]
            
            elif end < newInterval[0]:
                result.append([start, end])
            
            else:
                mergeStart = min(start, newInterval[0])
                mergeEnd = max(end, newInterval[1])
                newInterval = [mergeStart, mergeEnd]
        
        result.append(newInterval)
        return result