class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = []
        for s in strs:
            newStr.append(s)
            newStr.append("😃")
        return "".join(newStr)

    def decode(self, s: str) -> List[str]:
        strs = []
        current = []
        for c in s:
            if c == "😃":
                strs.append("".join(current))
                current = []
            else:
                current.append(c)
        return strs