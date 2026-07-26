class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Map = defaultdict(int)
        for c in s1:
            s1Map[c] += 1
        
        window = defaultdict(int)
        for i in range(len(s1)):
            window[s2[i]] += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if window == s1Map:
                return True
            
            window[s2[r]] += 1
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1
        
        return window == s1Map