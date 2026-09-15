from collections import deque
from heapq import heapify, heappush, heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        for t in tasks:
            counts[t] += 1
        
        heap = [-c for c in counts.values()]
        heapify(heap)
        q = deque()

        time = 0
        while heap or q:
            time += 1

            if heap:
                task = heappop(heap) + 1
                if task:
                    q.append([task, time + n])

            if q and q[0][1] == time:
                heappush(heap, q.popleft()[0])
        
        return time