class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        longest = 0
        mode = 0

        l = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            mode = max(mode, counts[s[r]])

            while (r - l + 1) - mode > k:
                counts[s[l]] -= 1
                l += 1
            longest = max(longest, (r - l + 1))
        
        return longest