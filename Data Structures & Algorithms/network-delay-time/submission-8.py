from heapq import heapify, heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(n + 1)}
        for u, v, w in times:
            adj[u].append((v, w))
        heap = [(0, k)]
        visited = set()

        time = 0
        while heap:
            w1, n1 = heappop(heap)
            if n1 in visited:
                continue
            
            time = w1
            visited.add(n1)

            for n2, w2 in adj[n1]:
                if n2 in visited:
                    continue
                heappush(heap, (w2 + time, n2))
        
        return time if len(visited) == n else -1