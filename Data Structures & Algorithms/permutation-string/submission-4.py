class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map, s2map = defaultdict(int), defaultdict(int)
        for c in s1:
            s1map[c] += 1
        
        for r in range(len(s1) - 1):
            s2map[s2[r]] += 1
        
        l = 0
        for r in range(len(s1) - 1, len(s2)):
            s2map[s2[r]] += 1
            if s1map == s2map:
                return True
            
            s2map[s2[l]] -= 1
            if s2map[s2[l]] == 0:
                del s2map[s2[l]]
            l += 1
        
        return False
