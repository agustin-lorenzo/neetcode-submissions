from heapq import heapify, heappop, heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: set() for i in range(n + 1)}
        for u, v, t in times:
            adj[u].add((v, t))
        
        visited = set()
        heap = [(0, k)]
        time = 0
        while heap:
            t1, n1 = heappop(heap)
            if n1 in visited:
                continue
            
            time = t1
            visited.add(n1)

            for n2, t2 in adj[n1]:
                if n2 in visited:
                    continue
                heappush(heap, (t2 + time, n2))
        
        return time if len(visited) == n else -1
