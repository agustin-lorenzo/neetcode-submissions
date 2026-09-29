from heapq import heapify, heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(n + 1)}
        for u, v, t in times:
            adj[u].append([v, t])
        
        heap = [[0, k]]
        visited = set()

        t = 0
        while heap:
            t1, n1 = heappop(heap)
            if n1 in visited:
                continue
            
            t = t1
            visited.add(n1)

            for n2, t2 in adj[n1]:
                if n2 in visited:
                    continue
                heappush(heap, [t + t2, n2])
        return t if len(visited) == n else -1