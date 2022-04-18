class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS ={}
        mapT = {}
        
        for i in s:
            mapS[i] = mapS.get(i,0) + 1
        
        for i in t:
            mapT[i] = mapT.get(i,0) + 1
        
        
        return mapS == mapT