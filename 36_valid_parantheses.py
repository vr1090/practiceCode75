# remove them from consideration
# remove these two as well

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}":"{","]":"[", ")":"(" }
        
        for c in s:
            if c in closeToOpen and stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            elif c in closeToOpen:
                return False
            else:
                stack.append(c)
        
        return len(stack) == 0 