class Solution:
    def isValid(self, s: str) -> bool:
        open2close = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for c in s:
            if c not in open2close:
                if not stack or c != open2close[stack.pop()]:
                    return False
            
            else:
                stack.append(c)

        return not stack

