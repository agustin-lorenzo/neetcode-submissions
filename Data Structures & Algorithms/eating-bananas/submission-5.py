class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(k):
            t = 0
            for p in piles:
                t += math.ceil(p / k)
            return t <= h

        l, r = 1, max(piles)
        minK = r
        while l <= r:
            m = (l + r) // 2
            if check(m):
                r = m - 1
                minK = m
            else:
                l = m + 1
        
        return minK