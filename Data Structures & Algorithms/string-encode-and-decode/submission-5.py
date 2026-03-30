class Solution:

    def encode(self, strList) -> str:
        result = ""
        for s in strList:
            result += s
            result += "@@"
        return result
    
    def decode(self, s) -> list[str]:
        result = []
        currentStr = ""
        i = 0
        while i < len(s):
            if s[i] == "@" and s[i + 1] == "@":
                result.append(currentStr)
                currentStr = ""
                i += 2
            else:
                currentStr += s[i]
                i += 1
        return result
