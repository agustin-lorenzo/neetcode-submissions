from heapq import heappush, heappop, heapify
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-c for c in counts.values()]
        heapify(heap)
        q = deque()

        t = 0
        while heap or q:
            t += 1
            if heap:
                remaining = heappop(heap) + 1
                if remaining:
                    q.append([remaining, t + n])
            
            if q and q[0][1] == t:
                heappush(heap, q.popleft()[0])
        
        return t