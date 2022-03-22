class Solution:
    def rob(self, nums: List[int]) -> int:
        def rauber(num):
            if len(num) == 0:
                return 0
            
            dp = [0] * len(num)
            
            for i in range(len(num)):
                left = dp[i-1] if i-1 >=0 else 0
                lef2 = dp[i-2] if i-2 >= 0 else 0
                
                dp[i] = max( left, lef2+num[i])
            
            
            return dp[len(num)-1]
        
        
        list1 = nums[:-1]
        list2 = nums[1:]
        
        
        return max(nums[0], rauber(list1), rauber(list2))