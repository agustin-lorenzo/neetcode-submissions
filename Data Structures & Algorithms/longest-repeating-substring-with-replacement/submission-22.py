class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        counts = {}

        l = 0
        for r in range(len(s)):
            rc = s[r]
            counts[rc] = counts.get(rc, 0) + 1
            while (r - l + 1) - max(counts.values()) > k:
                lc = s[l]
                counts[lc] -= 1
                l += 1
            
            longest = max(longest, (r - l + 1))
        
        return longest