class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [x] 1 <= k = max(piles)
        # [x] helper function that returns a boolean for a given k
        # [ ] binary search on range of possible k values
        #      * shift l & r depending on helper(k)

        def check(k):
            t = 0
            for p in piles:
                t += math.ceil(p / k)
                if t > h:
                    return False
            return True

        l = 1
        r = result = max(piles)
        while l <= r:
            k = (l + r) // 2
            if check(k):
                result = k
                r = k - 1
            else:
                l = k + 1
        
        return result