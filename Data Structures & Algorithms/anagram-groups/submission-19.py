class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            counts = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                counts[i] += 1
            if tuple(counts) not in groups:
                groups[tuple(counts)] = []
            groups[tuple(counts)].append(s)
        
        return list(groups.values())