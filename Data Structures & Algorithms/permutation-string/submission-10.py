class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        map1 = {}
        for c in s1:
            map1[c] = map1.get(c, 0) + 1
        
        map2 = {}
        for i in range(0, len(s1) - 1):
            map2[s2[i]] = map2.get(s2[i], 0) + 1
        
        l = 0
        for r in range(len(s1) - 1, len(s2)):
            rc = s2[r]
            map2[rc] = map2.get(rc, 0) + 1
            if map1 == map2:
                return True
            
            lc = s2[l]
            map2[lc] -= 1
            if map2[lc] == 0:
                del map2[lc]
            l += 1
        
        return False
