class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pos = len(digits) - 1
        additional = 1
        
        while additional > 0 and pos >= 0 :
            currentAddPlusPos = digits[pos] + additional
            additional = currentAddPlusPos // 10
            digits[pos] = currentAddPlusPos % 10
            pos = pos -1
        
        
        if additional > 0:
            return [1] + digits
        else:
            return digits