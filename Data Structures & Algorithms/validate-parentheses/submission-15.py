class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open2Close = {'(': ')', '[': ']', '{': '}'}

        for c in s:
            if c in open2Close:
                stack.append(c)
            else:
                if not stack or open2Close[stack.pop()] != c:
                    return False

        return True if not stack else False
