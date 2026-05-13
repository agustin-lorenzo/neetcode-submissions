class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        window = [0] * 26

        l = 0
        for r in range(len(s)):
            ri = ord(s[r]) - ord('A')
            window[ri] += 1

            while (r - l + 1) - max(window) > k:
                li = ord(s[l]) - ord('A')
                window[li] -= 1
                l += 1
            
            longest = max(longest, (r - l + 1))
        
        return longest