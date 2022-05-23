class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0
        charMap = {}
        res = 0
        
        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r],0) + 1
            
            while len(charMap) > k:
                charMap[s[l]] = charMap[s[l]] - 1
                
                if(charMap[s[l]] ==0):
                    del charMap[s[l]]
                
                l = l + 1
            
            res = max(res, r-l +1)
        
        return res
            
            