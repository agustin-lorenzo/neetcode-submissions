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
            k = (l + r) // 2
            if check(k):
                r = k - 1
                minK = k
            else:
                l = k + 1
        
        return minK