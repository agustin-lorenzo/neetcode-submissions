class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window of length = len(s1)
        # as window slides over s2, compare substring of s2 against s1
        # comparison be done with hashmaps that contain char: count

        def getMap(s):
            sMap = {}
            for c in s:
                sMap[c] = sMap.get(c, 0) + 1
            return sMap

        s1Map = getMap(s1)
        l, r = 0, len(s1) - 1

        while r < len(s2):
            s2Map = getMap(s2[l:r+1])
            if s1Map == s2Map:
                return True
            l += 1
            r += 1
            
        return False
