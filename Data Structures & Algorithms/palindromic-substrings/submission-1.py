class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        def countPali(l, r):
            nonlocal result
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1        

        for i in range(len(s)):
            countPali(i, i)
            countPali(i, i + 1)
        
        return result