from collections import deque, Counter
from heapq import heapify, heappush, heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-freq for freq in counts.values()]
        heapify(heap)
        q = deque()

        time = 0
        while q or heap:
            time += 1

            if heap:
                task = heappop(heap) + 1
                if task:
                    q.append([task, time + n])

            if q and time == q[0][1]:
                heappush(heap, q.popleft()[0])
        
        return time
