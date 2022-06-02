class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        for i in range(1, (len(s)//2)+1 ):
            if len(s) % i == 0 :
                strNew = s[0:i]
                lenStr =len(s[0:i])
                count = len(s)// lenStr
                
                if (strNew * count) == s:
                    return True
        
        return False
        
        