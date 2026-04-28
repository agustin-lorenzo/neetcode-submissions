class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            t = 0
            for p in piles:
                t += math.ceil(p / k)
            return t <= h
        
        l = 1
        r = mink = max(piles)
        while l <= r:
            m = (l + r) // 2
            if check(m):
                mink = m
                r = m - 1
            else:
                l = m + 1
        
        return mink