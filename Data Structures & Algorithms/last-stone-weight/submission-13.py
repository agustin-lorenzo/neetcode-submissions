import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1, s2 = -heapq.heappop(stones), -heapq.heappop(stones)
            newStone = s1 - s2
            if newStone:
                heapq.heappush(stones, -newStone)
            
        return -stones[0] if stones else 0