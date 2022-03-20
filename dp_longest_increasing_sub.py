class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        maximum = 1
        
        for i in range(len(nums) ):
            localMax = 1
            
            for j in range(i):
                if nums[j] < nums[i]:
                    localMax = max(localMax, 1 + dp[j])
                
                dp[i] = localMax
                maximum = max(dp[i], maximum)
        
        return maximum
