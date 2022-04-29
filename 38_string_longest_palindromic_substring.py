class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        currentLen = 0
        
        for i in range(len(s)):
            odd = self.findPalinFromPos(s,i,i)
            even = self.findPalinFromPos(s,i,i+1)
            pickup = odd if len(odd) > len(even) else even
            
            if len(pickup) > currentLen:
                currentLen = len(pickup)
                result = pickup
            
        return result
    
        
    def findPalinFromPos(self,s, l, r):
        result = ""

        while l>= 0 and r< len(s) and s[l] == s[r]:

            if( r -l + 1 > len(result)):
                result = s[l:r+1]

            l = l - 1
            r = r + 1

        return result
