class Solution:
    def isValid(self, s: str) -> bool:
        open2Close = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for c in s:
            if c not in open2Close:
                if not stack or open2Close[stack.pop()] != c:
                    return False
            
            else:
                stack.append(c)

        if not stack:
            return True
        return False