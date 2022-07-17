class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        
        winS = {}
        winT = {}
        length = float("infinity")
        
        
        for i in range(len(t)):
            winT[t[i]] = winT.get( t[i], 0) + 1
        
        have = 0
        want = len(winT)
        resL = 0
        resR = 0
        l =0
        
        for r in range(len(s)):
            charR = s[r]
            winS[charR] = winS.get(charR, 0) + 1
            
            if charR in t and winS[charR] == winT[charR]:
                have = have + 1
                
            while have == want:
                
                if ( r-l + 1) < length:
                    length = r-l+ 1
                    resL = l
                    resR = r
                
                #make it smaller 
                winS[s[l]] = winS[s[l]] - 1
                
                if s[l] in t and winS[s[l]] < winT[s[l]]:
                    have -= 1
                
                l = l + 1
        
        return s[resL:resR+1] if length != float("infinity") else ""
        
        
        
                
                
                