class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        result = ""
        bestLen = float("inf")
        tmap, window = defaultdict(int), defaultdict(int)
        have = 0
        for c in t:
            tmap[c] += 1
        need = len(tmap)
        
        l = 0
        for r in range(len(s)):
            if s[r] in tmap:
                window[s[r]] += 1
                if window[s[r]] == tmap[s[r]]:
                    have += 1
                
            while have == need:
                if r - l + 1 < bestLen:
                    result = s[l:r + 1]
                    bestLen = len(result)

                if s[l] in tmap:
                    if window[s[l]] == tmap[s[l]]:
                        have -= 1
                    window[s[l]] -= 1
                l += 1
        return result
        
