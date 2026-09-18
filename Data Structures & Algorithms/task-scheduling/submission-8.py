from heapq import heappush, heappop, heapify
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [-c for c in counter.values()]
        heapify(heap)
        q = deque()

        time = 0
        while heap or q:
            time += 1
            if heap:
                remaining = heappop(heap) + 1
                if remaining:
                    q.append([remaining, time + n])
            
            if q and q[0][1] == time:
                heappush(heap, q.popleft()[0])
        
        return time