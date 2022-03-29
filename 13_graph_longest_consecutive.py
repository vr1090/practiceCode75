class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNumber = set(nums)
        maxCount = 0
        
        for n in nums:
            count = 0
            
            # are we in the first?
            if n-1 not in setNumber:
                count =0
            
                while n + count in setNumber:
                    count = count + 1
                
                maxCount = max(maxCount, count)
        
        return maxCount