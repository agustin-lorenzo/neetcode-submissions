class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1, map2 = defaultdict(int), defaultdict(int)
        for c in s1:
            map1[c] += 1
        
        for i in range(len(s1) - 1):
            map2[s2[i]] += 1
        
        l = 0
        for r in range(len(s1) - 1, len(s2)):
            map2[s2[r]] += 1
            if map1 == map2:
                return True
            
            map2[s2[l]] -= 1
            if map2[s2[l]] == 0:
                del map2[s2[l]]
            l += 1
        
        return False