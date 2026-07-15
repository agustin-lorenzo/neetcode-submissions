class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        resultLen = float("inf")

        window = defaultdict(int)
        tmap = defaultdict(int)
        for c in t:
            tmap[c] += 1
        need = len(tmap)
        have = 0
        
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == tmap[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < resultLen:
                    result = s[l:r+1]
                    resultLen = r - l + 1
                
                if window[s[l]] == tmap[s[l]]:
                    have -= 1
                window[s[l]] -= 1
                l += 1
        
        return result