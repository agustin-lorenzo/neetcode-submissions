class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        result = ""
        minLen = float("inf")
        tmap, window = defaultdict(int), defaultdict(int)
        have = need = 0

        for c in t:
            tmap[c] += 1
        need = len(tmap)

        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in tmap:
                window[c] += 1
                if window[c] == tmap[c]:
                    have += 1
                
            while have == need:
                if r - l + 1 < minLen:
                    result = s[l:r+1]
                    minLen = len(result)

                lc = s[l]
                if lc in tmap:
                    if window[lc] == tmap[lc]:
                        have -= 1
                    window[lc] -= 1
                l += 1

        return result