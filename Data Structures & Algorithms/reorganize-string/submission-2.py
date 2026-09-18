from heapq import heapify, heappush, heappop
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = [[-count, char] for char, count in counts.items()]
        heapify(heap)

        result = []
        prev = None
        while heap:
            count, char = heappop(heap)
            result.append(char)
            count += 1

            if prev:
                heappush(heap, prev)
                prev = None

            if count:
                prev = [count, char]
        
        return "".join(result) if len(result) == len(s) else ""