class Solution:
    def scoreOfString(self, s: str) -> int:
        l, r = 0, 1
        total = 0

        while r < len(s):
            total += abs(ord(s[r]) - ord(s[l]))
            r += 1
            l += 1

        return total