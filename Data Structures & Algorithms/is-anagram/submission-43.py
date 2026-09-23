class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        smap, tmap = {}, {}
        for i in range(len(s)):
            sc, tc = s[i], t[i]
            smap[sc] = smap.get(sc, 0) + 1
            tmap[tc] = tmap.get(tc, 0) + 1
        
        return smap == tmap