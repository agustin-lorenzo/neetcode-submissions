class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap, tMap = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            sc, tc = s[i], t[i]
            sMap[sc] += 1
            tMap[tc] += 1
        
        return sMap == tMap
