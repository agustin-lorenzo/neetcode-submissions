class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def getKey(s):
            key = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                key[index] += 1
            return tuple(key)

        groups = {}
        for s in strs:
            sKey = getKey(s)
            if sKey not in groups:
                groups[sKey] = []
            groups[sKey].append(s)
        
        return list(groups.values())
