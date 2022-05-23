class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        fruitMap = {}
        maxBasket = 2
        res = 0
        
        for r in range(len(fruits)):
            key = fruits[r]
            fruitMap[key] = fruitMap.get( key, 0) + 1
            
            while len(fruitMap) > maxBasket:
                keyL = fruits[l]
                fruitMap[keyL] = fruitMap[keyL] - 1
                
                if fruitMap[keyL] == 0:
                    del fruitMap[keyL]
                l = l + 1
            
            res = max( res, r-l + 1)
        
        return res
            