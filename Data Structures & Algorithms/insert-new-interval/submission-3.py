class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            start, end = intervals[i]
            if end < newInterval[0]:
                result.append([start, end])
            
            elif start > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]
            
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
        
        result.append(newInterval)
        return result
