class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapChar ={}
        
        for s1 in s:
            mapChar[s1] = mapChar.get(s1,0) + 1
        print(mapChar)
        for idx, ch in enumerate(s):
            if mapChar[ch] == 1:
                return idx
        
        return -1