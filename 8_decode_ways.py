class Solution:
    def numDecodings(self, s: str) -> int:
        res = {len(s): 1}
        
        def helper(pos):
            if (s[pos] == "0"):
                res[pos] = 0
            else:
                res[pos] = res[pos+1]
            
            if pos+1 < len(s):
                if s[pos] == "1":
                    res[pos] += res[pos+2]
                elif s[pos] =="2" and s[pos+1] in "0123456":
                    res[pos] += res[pos+2]
        
        for i in range(len(s)-1,-1,-1):
            helper(i)
        
        return res[0]
            