class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def matches(sa,sb):
            for i in range(len(sa)):
                if sa[i] != sb[i]:
                    return False
            
            return True
    
        
        if len(s1) > len(s2):
            return False
        
        s1Map = {i:0 for i in range(26)}
        s2Map = {i:0 for i in range(26)}
        
        for i in range(len(s1)):
            s1Map[ord(s1[i]) -ord("a")] = s1Map.get(ord(s1[i])-ord("a"),0)+1
            s2Map[ord(s2[i])-ord("a")] = s2Map.get( ord(s2[i])-ord("a"),0)+1
        
        lenS1 = len(s1)
        
        for i in range(len(s2)-len(s1)):
            if matches(s1Map, s2Map):
                return True
            
            s2Map[ord(s2[i+lenS1])-ord("a")] = s2Map.get(ord(s2[i+lenS1])-ord('a'),0) + 1
            s2Map[ord(s2[i])-ord('a')] =s2Map[ord(s2[i])-ord('a')] - 1
        
        return matches(s1Map, s2Map)
        