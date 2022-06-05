class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        pos = len(num) - 1
        additional = k
        
        while additional > 0 and pos >= 0 :
            currentAddPlusPos = num[pos] + additional
            additional = currentAddPlusPos // 10
            num[pos] = currentAddPlusPos % 10
            pos = pos -1
        
        
        while additional > 0:
            newAddition = additional
            additional = newAddition // 10
            num = [newAddition % 10] + num
        
        return num
        