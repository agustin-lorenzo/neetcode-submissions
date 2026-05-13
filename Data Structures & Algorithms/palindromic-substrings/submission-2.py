class Solution:
    def countSubstrings(self, s: str) -> int:
        numSubstrings = 0

        def countPali(l, r):
            result = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
            return result

        for i in range(len(s)):
            numSubstrings += countPali(i, i)
            numSubstrings += countPali(i, i + 1)
        
        return numSubstrings