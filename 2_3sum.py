class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i,a in enumerate(nums):
            
            if i > 0 and a == nums[i-1]:
                continue
            
            # got the a
            
            l = i + 1
            r = len(nums) -1
            
            while l < r:
                sumAll = a + nums[l] + nums[r]
                
                if sumAll < 0:
                    l = l + 1
                elif sumAll > 0:
                    r = r-1
                else:
                    result.append([a,nums[l], nums[r]])
                    l =l+1
                    
                    while l < r and nums[l] == nums[l-1]:
                        l = l + 1
        
        return result