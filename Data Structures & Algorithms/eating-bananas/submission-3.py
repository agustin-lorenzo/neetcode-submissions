class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [x] 1 <= k = max(piles)
        # [x] helper function that returns a boolean for a given k
        # [ ] binary search on range of possible k values
        #      * shift l & r depending on helper(k)

        l, r = 1, max(piles)
        result = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                result = min(result, k)
                r = k - 1
            else:
                l = k + 1
        
        return result