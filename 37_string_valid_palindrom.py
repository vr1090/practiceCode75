class Solution:
    def isPalindrome(self, s: str) -> bool:
        compact = []
        
        for i in s:
            if self.isAlnum(i):
                compact.append(i.lower() )
                
        
        l = 0 
        r = len(compact) -1
        
        while l < r:
            if compact[l] != compact[r]:
                return False
            
            l = l + 1
            r = r -1 
        
        return True
    
    def isAlnum(self, c):
        ordC = ord(c)
        
        return (ordC >= ord("A") and ordC <=ord("Z")) \
            or (ordC >= ord("a") and ordC <=ord("z")) \
            or (ordC >= ord("0") and ordC <= ord("9"))