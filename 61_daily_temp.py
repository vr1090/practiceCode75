class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        result = [0] * len(temp)
        stack = []
        
        for curP, curT in enumerate(temp):
            
            while stack and temp[stack[-1]] < curT:
                pos = stack.pop()
                result[pos] = curP- pos
            
            stack.append(curP)
        
        return result