class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            for c in s:
                result.append(c)
            result.append("ƒ")
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        strs = []
        current = []
        for c in s:
            if c == "ƒ":
                strs.append("".join(current))
                current = []
            else:
                current.append(c)
        return strs