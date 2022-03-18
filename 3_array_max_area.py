class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxCon = 0
        l = 0
        r = len(height) - 1
        
        while l < r:
            h = min(height[l], height[r])
            d = r -l
            
            maxCon = max(maxCon, h * d)
            
            if height[l] < height[r]:
                l = l +1
            else:
                r = r- 1
        
        return maxCon