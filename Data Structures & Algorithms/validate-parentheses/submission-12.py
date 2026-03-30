class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in openToClose:
                stack.append(c)
                continue
            if not stack or openToClose[stack.pop()] != c:
                return False      

        if not stack:
            return True
        return False