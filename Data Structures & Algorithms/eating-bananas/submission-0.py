class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkRate(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
                if hours > h:
                    return False
            return True
        
        lower, upper = 1, max(piles)
        minK = upper
        while lower <= upper:
            mid = (lower + upper) // 2
            if checkRate(mid) == True:
                upper = mid - 1
                minK = mid
            else:
                lower = mid + 1
        
        return minK