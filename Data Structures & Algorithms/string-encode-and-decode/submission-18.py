class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(s)
            result.append("ƒ")
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        current = []
        for c in s:
            if c == "ƒ":
                result.append("".join(current))
                current = []
            else:
                current.append(c)
        return result