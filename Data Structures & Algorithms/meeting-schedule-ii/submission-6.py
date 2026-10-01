"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heapify, heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        result = 0
        heap = []

        for i in range(len(intervals)):
            interval = intervals[i]
            while heap and interval.start >= heap[0]:
                heappop(heap)
            
            heappush(heap, interval.end)
            result = max(result, len(heap))
        
        return result