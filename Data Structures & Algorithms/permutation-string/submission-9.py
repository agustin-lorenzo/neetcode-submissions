class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window, s1map = defaultdict(int), defaultdict(int)

        for c in s1:
            s1map[c] += 1

        for i in range(len(s1) - 1):
            window[s2[i]] += 1
        
        l = 0
        for r in range(len(s1) - 1, len(s2)):
            window[s2[r]] += 1
            if window == s1map:
                return True
            
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1
        
        return False