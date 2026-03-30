class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result, resLen = "", float("inf")
        
        smap, tmap = defaultdict(int), defaultdict(int)
        for c in t:
            tmap[c] += 1
        need = len(tmap)
        have = 0

        l = 0
        for r in range(len(s)):
            smap[s[r]] += 1
            if smap[s[r]] == tmap[s[r]]:
                have += 1
            
            while have >= need:
                if r - l + 1 < resLen:
                    result = s[l:r+1]
                    resLen = r - l + 1

                if smap[s[l]] == tmap[s[l]]:
                    have -= 1
                smap[s[l]] -= 1
                l += 1
        
        return result