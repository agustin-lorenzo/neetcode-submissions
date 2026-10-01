from heapq import heapify, heappush, heappop
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = [[-count, char] for char, count in counter.items()]
        heapify(heap)
        result = []
        prev = None

        while heap:
            remaining, char = heappop(heap)
            remaining += 1
            result.append(char)

            if prev:
                heappush(heap, prev)
                prev = None
            
            if remaining:
                prev = [remaining, char]
        
        return "".join(result) if len(result) == len(s) else ""