from functools import cache

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        @cache
        def check(k):
            t = 0
            for p in piles:
                t += math.ceil(p / k)
            return t <= h
        
        minK = max(piles)
        l, r = 1, minK
        while l <= r:
            k = (l + r) // 2
            if check(k):
                minK = k
                r = k - 1
            else:
                l = k + 1
        
        return minK