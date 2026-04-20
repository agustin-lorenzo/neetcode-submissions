class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        length = len(min(strs, key=len))
        for i in range(length):
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return result
            result += c
        
        return result