from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        visited = set()
        heap = [(0, k)]
        t = 0
        while heap:
            w1, n1 = heappop(heap)
            if n1 in visited:
                continue
            
            t = w1
            visited.add(n1)
            
            for n2, w2 in edges[n1]:
                if n2 in visited:
                    continue
                heappush(heap, (w1 + w2, n2))
        
        return t if len(visited) == n else -1