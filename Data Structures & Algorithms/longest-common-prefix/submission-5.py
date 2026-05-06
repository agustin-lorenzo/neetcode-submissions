class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []

        for i in range(len(min(strs))):
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return "".join(result)
            result.append(c)
        
        return "".join(result)