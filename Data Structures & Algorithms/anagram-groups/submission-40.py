class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            chars = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                chars[i] += 1
            
            key = tuple(chars)
            if key not in groups:
                groups[key] = []
            
            groups[key].append(s)
        
        return list(groups.values())