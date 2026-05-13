class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        for c in s1:
            s1Map[c] = s1Map.get(c, 0) + 1
        
        window = {}
        for i in range(len(s1) - 1):
            window[s2[i]] = window.get(s2[i], 0) + 1
        
        l = 0
        for r in range(len(s1) - 1, len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1
            if window == s1Map:
                return True
            
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1
        
        return False