class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        window = set()

        l = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            
            window.add(s[r])
            result = max(result, (r - l + 1))
        
        return result