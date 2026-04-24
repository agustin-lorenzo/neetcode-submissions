class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        if len(s) == 0:
            return True

        sp = 0
        for c in t:
            sc = s[sp]
            if c == sc:
                sp += 1
                if sp == len(s):
                    return True

        return False