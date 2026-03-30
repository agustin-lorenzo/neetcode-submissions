class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        for c in s1:
            s1Map[c] = s1Map.get(c, 0) + 1

        left = 0
        for right in range(len(s1), len(s2) + 1):
            subString = s2[left:right]

            currentMap = {}
            for c in subString:
                currentMap[c] = currentMap.get(c, 0) + 1
            
            if currentMap == s1Map:
                return True

            left += 1
        
        return False