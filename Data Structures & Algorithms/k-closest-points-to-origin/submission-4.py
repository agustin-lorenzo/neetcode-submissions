class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [[x**2 + y**2, x, y] for x, y in points]
        heapq.heapify(dist)
        result = []

        while len(result) < k:
            d, x, y = heapq.heappop(dist)
            result.append([x, y])
        
        return result