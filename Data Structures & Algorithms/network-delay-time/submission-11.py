from heapq import heappop, heappush, heapify

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(n + 1)}
        for u, v, t in times:
            adj[u].append([v, t])
        
        time = 0
        heap = [[0, k]]
        visited = set()

        while heap:
            t1, n1 = heappop(heap)
            if n1 in visited:
                continue
            
            visited.add(n1)
            time = t1

            for n2, t2 in adj[n1]:
                if n2 in visited:
                    continue
                heappush(heap, [time + t2, n2])
        
        return time if len(visited) == n else -1