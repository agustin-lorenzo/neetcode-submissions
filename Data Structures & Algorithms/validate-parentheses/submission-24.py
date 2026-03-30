class Solution:
    def isValid(self, s: str) -> bool:
        close2open = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c in close2open:
                if not stack or close2open[c] != stack.pop():
                    return False
            
            else:
                stack.append(c)

        return not stack