class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {'}': '{', ')': '(', ']': '['}

        for c in s:
            if stack and c in closeToOpen:
                if stack.pop() != closeToOpen[c]:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False