class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque() # pairs of [-count, idle time]

        while maxHeap or q:
            time += 1
            if maxHeap:
                count = heapq.heappop(maxHeap) + 1 
                if count:
                    q.append([count, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
