class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        result = ""
        resLen = float("inf")

        window = {}
        tMap = {}
        for c in t:
            tMap[c] = tMap.get(c, 0) + 1
        need = len(tMap)
        have = 0

        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in tMap and window[s[r]] == tMap[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    result = s[l:r+1]

                if s[l] in tMap and window[s[l]] == tMap[s[l]]:
                    have -= 1
                window[s[l]] -= 1
                l += 1
        
        return result