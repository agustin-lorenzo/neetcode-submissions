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
            key = getKey(s)
            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())