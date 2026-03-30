class Solution:
    def isValid(self, s: str) -> bool:
        close2open = {'}': '{', ')': '(', ']': '['}
        stack = []

        for c in s:
            if c in close2open and (not stack or close2open[c] != stack.pop()):
                return False
            if c not in close2open:
                stack.append(c)

        return not stack