class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        bestLen = float("inf")
        tmap, window = {}, {}
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1
        need = len(tmap)
        have = 0

        l = 0
        for r in range(len(s)):
            if s[r] in tmap:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == tmap[s[r]]:
                    have += 1
            
            while have == need:
                if r - l + 1 < bestLen:
                    result = s[l:r+1]
                    bestLen = r - l + 1

                lc = s[l]
                if lc in tmap:
                    if window[lc] == tmap[lc]:
                        have -= 1
                    window[lc] -= 1
                l += 1

        return result