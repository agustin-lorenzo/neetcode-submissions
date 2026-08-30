from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)

        while len(stones) > 1:
            s1, s2 = -heappop(stones), -heappop(stones)
            newStone = -abs(s1 - s2)
            heappush(stones, newStone)
        
        return -stones[0] if stones else 0