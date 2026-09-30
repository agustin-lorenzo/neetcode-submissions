"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappush, heappop, heapify

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        result = 0
        heap = []

        for i in range(len(intervals)):
            start, end = intervals[i].start, intervals[i].end

            while heap and start >= heap[0]:
                heappop(heap)
            
            heappush(heap, end)
            result = max(result, len(heap))
        
        return result