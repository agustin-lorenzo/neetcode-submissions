

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = [[-count, char] for char, count in counter.items()]
        heapq.heapify(heap)

        result = []
        prev = None
        while heap:
            count, char = heapq.heappop(heap)
            count += 1
            result.append(char)

            if prev:
                heapq.heappush(heap, prev)
                prev = None
            
            if count:
                prev = [count, char]
        
        return "".join(result) if len(result) == len(s) else ""