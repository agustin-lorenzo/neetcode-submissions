class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = [0] * 1000

        l = 0
        for r in range(len(s)):
            ridx = ord(s[r]) - ord('a')
            while window[ridx] == 1:
                lidx = ord(s[l]) - ord('a')
                if window[lidx] == 1:
                    window[lidx] -= 1
                l += 1
            
            window[ridx] = 1
            length = r - l + 1
            longest = max(longest, length)
        
        return longest