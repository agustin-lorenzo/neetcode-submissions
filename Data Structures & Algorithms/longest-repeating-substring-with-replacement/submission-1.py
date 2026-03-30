class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCounts = {}
        mostFreq = s[0]
        longest = 0

        l = 0
        for r in range(len(s)):
            charCounts[s[r]] = charCounts.get(s[r], 0) + 1
            if charCounts[s[r]] > charCounts[mostFreq]:
                mostFreq = s[r]
            
            valid = ((r - l + 1) - charCounts[mostFreq]) <= k
            if valid:
                longest = max(longest, (r - l + 1))
            else:
                charCounts[s[l]] -= 1
                l += 1
        
        return longest