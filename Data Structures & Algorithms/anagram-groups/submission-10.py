class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                i = ord('a') - ord(c)
                key[i] += 1
            groups[tuple(key)].append(s)
        
        return list(groups.values())

