class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        substring = ""

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # after exiting the loop, l and r aren't valid
            # return PREVIOUS l and r indicies
            return s[l + 1:r]
        
        for i in range(len(s)):
            even = expand(i, i + 1)
            if len(even) > longest:
                longest = len(even)
                substring = even
            
            odd = expand(i, i)
            if len(odd) > longest:
                longest = len(odd)
                substring = odd
            
        return substring