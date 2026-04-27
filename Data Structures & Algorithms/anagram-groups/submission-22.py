class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            key = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                key[i] += 1
            if tuple(key) not in groups:
                groups[tuple(key)] = []
            groups[tuple(key)].append(s)
        
        return list(groups.values())
