class Solution:
    def isValid(self, s: str) -> bool:
        close2Open = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in close2Open:
                if not stack or close2Open[c] != stack.pop():
                    return False
            else:
                stack.append(c)

        return not stack