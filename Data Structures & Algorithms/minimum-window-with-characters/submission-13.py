class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        minLength = float("inf")

        tmap = {}
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1
        need = len(tmap)
        have = 0

        window = {}
        l = 0
        for r in range(len(s)):
            rc = s[r]
            window[rc] = window.get(rc, 0) + 1
            if rc in tmap and tmap[rc] == window[rc]:
                have += 1
            
            while have == need:
                if (r - l + 1) < minLength:
                    result = s[l:r+1]
                    minLength = r - l + 1
                lc = s[l]
                if lc in tmap and window[lc] == tmap[lc]:
                    have -= 1
                window[lc] -= 1
                l += 1
        
        return result

