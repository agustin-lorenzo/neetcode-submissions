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
            count, char = heappop(heap)
            result.append(char)

            if prev:
                heappush(heap, prev)
                prev = None
            
            count += 1
            if count:
                prev = [count, char]
        
        return "".join(result) if len(result) == len(s) else ""