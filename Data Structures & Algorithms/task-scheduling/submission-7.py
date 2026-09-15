from heapq import heapify, heappush, heappop
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
                task = heappop(heap) + 1
                if task:
                    q.append([task, time + n])
            
            if q and q[0][1] == time:
                heappush(heap, q.popleft()[0])
        
        return time