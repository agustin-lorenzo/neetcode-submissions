class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap, tMap = {}, {}
        for i in range(len(s)):
            sc, tc = s[i], t[i]
            sMap[sc] = sMap.get(sc, 0) + 1
            tMap[tc] = tMap.get(tc, 0) + 1

        return sMap == tMap