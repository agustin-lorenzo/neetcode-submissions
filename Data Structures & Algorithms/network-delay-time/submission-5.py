from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
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
                heappush(heap, (time + w2, n2))
        
        return time if len(visited) == n else -1