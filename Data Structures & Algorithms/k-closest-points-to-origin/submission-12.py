from heapq import heapify, heappop, heappush

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[x**2 + y**2, x, y] for x, y in points]
        heapify(distances)
        result = []

        while len(result) < k:
            d, x, y = heappop(distances)
            result.append([x, y])
        
        return result