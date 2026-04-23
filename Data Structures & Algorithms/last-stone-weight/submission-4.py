class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)
            if second > first:
                newStone = abs(first) - abs(second)
                heapq.heappush(stones, -newStone)

        return abs(stones[0]) if stones else 0