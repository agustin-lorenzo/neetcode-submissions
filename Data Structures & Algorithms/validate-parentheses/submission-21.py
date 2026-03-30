class Solution:
    def isValid(self, s: str) -> bool:
        open2Close = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for c in s:
            if c not in open2Close:
                if not stack or c != open2Close[stack.pop()]:
                    return False
            else:
                stack.append(c)
        
        return not stack
                