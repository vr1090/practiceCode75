class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            minimum = float("inf")
            changes = False
            for c in coins:
                if ( i-c >= 0 and dp[i-c] !=-1):
                    minimum = min(minimum, 1+ dp[i-c])
                    changes = True
                    
            dp[i] = minimum if changes else -1
        return dp[amount]