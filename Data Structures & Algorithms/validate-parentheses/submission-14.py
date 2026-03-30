class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {'}': '{', ']': '[', ')': '('}

        for c in s:
            if c not in closeToOpen:
                stack.append(c)
            else:
                if not stack:
                    return False
                openP = stack.pop()
                if openP != closeToOpen[c]:
                    return False
        
        if stack:
            return False

        return True
            

