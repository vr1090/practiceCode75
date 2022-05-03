class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(len(s)):
            count = count + self.countPalin(s,i,i ) +  self.countPalin(s,i,i+1)
        
        return count
    
    def countPalin(self, s, i1, i2):
        l , r = i1, i2
        count = 0
        
        while l >= 0 and r < len(s) and s[l] == s[r] :
            count = count + 1
            l = l -1 
            r = r + 1
        
        
        return count