class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        mapChar = {}
        l = 0
        
        for r in range(len(s)):
            mapChar[s[r]] = mapChar.get(s[r], 0) + 1
            
            while (r-l+1) - max( mapChar.values() ) > k:
                mapChar[s[l]] = mapChar[s[l]] -1
                l = l + 1
            
            result = max(result, r-l + 1)
        return result