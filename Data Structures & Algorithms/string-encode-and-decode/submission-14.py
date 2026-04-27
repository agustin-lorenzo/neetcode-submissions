class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += s
            result += '<>?'
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        current = []
        i = 0
        while i < len(s):
            if i < len(s) - 2 and s[i] == '<' and s[i+1:i+3] == ">?":
                result.append("".join(current))
                current = []
                i += 3
            else:
                current.append(s[i])
                i += 1
        return result