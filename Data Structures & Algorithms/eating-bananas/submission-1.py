class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkRate(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
                if hours > h:
                    return False
            return True

        minK, maxK = 1, max(piles)
        while minK < maxK:
            mid = (minK + maxK) // 2
            if checkRate(mid):
                maxK = mid
            else:
                minK = mid + 1
        
        return minK
