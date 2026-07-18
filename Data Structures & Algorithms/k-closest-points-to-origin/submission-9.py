class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[(x**2 + y**2), x, y] for x, y in points]
        heapq.heapify(distances)
        result = []
        
        while len(result) < k:
            d, x, y = heapq.heappop(distances)
            result.append([x, y])
        
        return result