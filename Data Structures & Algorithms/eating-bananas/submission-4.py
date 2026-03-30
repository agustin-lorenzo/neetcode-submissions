class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def checkRate(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            return hours <= h
        
        minK, maxK = 1, max(piles)
        result = maxK
        while minK <= maxK:
            k = (minK + maxK) // 2
            if checkRate(k):
                result = k
                maxK = k - 1
            else:
                minK = k + 1

        return result