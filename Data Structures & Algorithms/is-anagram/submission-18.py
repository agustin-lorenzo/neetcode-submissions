class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        smap, tmap = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            smap[s[i]] += 1
            tmap[t[i]] += 1
        
        return smap == tmap