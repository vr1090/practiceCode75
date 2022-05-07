class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""

        for s in strs:
            res += str( len(s) ) + "#"+s
        
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res = []
        l = 0

        while l < len(str):
            j = l

            while str[j] != "#":
                j = j +1
            
            number = int( str[l:j])

            res.append( str[j+1:j+1+number])

            l = j+1 + number
        
        return res
