"""
matches = 0

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if(len(s1) > len(s2)):
            return False
        
        matches = 0
        
        s1Map = [0] * 26
        s2Map = [0] * 26
        
        # initial 
        
        for i in range(len(s1)):
            s1Map[ ord(s1[i]) - ord('a')] += 1 
            s2Map[ ord(s2[i]) - ord("a")] += 1
        
        for i in range(26):
               matches += 1 if(s1Map[i] == s2Map[i]) else 0
        
        
        l =0 
        
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord("a")
            s2Map[index] += 1
            
            if s1Map[index] == s2Map[index]:
                matches += 1
            elif s1Map[index] + 1 == s2Map[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2Map[index] -= 1
            
            if(s1Map[index] == s2Map[index]):
                matches += 1
            elif s1Map[index] -1 == s2Map[index]:
                matches -= 1
            
            l = l + 1
            
        return matches == 26