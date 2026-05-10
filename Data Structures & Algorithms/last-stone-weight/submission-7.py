class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1, s2 = -heapq.heappop(stones), -heapq.heappop(stones)
            if s1 != s2:
                newStone = s1 - s2
                heapq.heappush(stones, -newStone)
        
        return -heapq.heappop(stones) if stones else 0