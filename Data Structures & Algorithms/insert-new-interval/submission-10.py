class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            start, end = intervals[i]

            if end < newInterval[0]:
                result.append([start, end])
            
            elif newInterval[1] < start:
                result.append(newInterval)
                return result + intervals[i:]
            
            else:
                newS = min(start, newInterval[0])
                newE = max(end, newInterval[1])
                newInterval = [newS, newE]
        
        result.append(newInterval)
        return result