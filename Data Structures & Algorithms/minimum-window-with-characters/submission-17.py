class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        result = ""
        resLen = float("inf")

        window = {}
        tmap = {}
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1
        need = len(tmap)
        have = 0

        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in tmap and tmap[s[r]] == window[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    result = s[l:r + 1]
                    resLen = (r - l + 1)

                if s[l] in tmap and window[s[l]] == tmap[s[l]]:
                    have -= 1
                window[s[l]] -= 1
                l += 1
        
        return result
