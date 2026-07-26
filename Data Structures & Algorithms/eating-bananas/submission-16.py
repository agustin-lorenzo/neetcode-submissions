class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(k):
            t = 0
            for p in piles:
                t += math.ceil(p / k)
            return t <= h
        
        minK = l = 1
        r = max(piles)
        while l <= r:
            m = (l + r) // 2
            if check(m):
                minK = m
                r = m - 1
            else:
                l = m + 1
        return minK