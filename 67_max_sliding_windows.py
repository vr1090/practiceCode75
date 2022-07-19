class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l =0
        result = []
        que = deque()
        
        for r in range(len(nums)):
            while que and nums[que[-1]] < nums[r]:
                que.pop()
            
            que.append(r)
            
            if(l > que[0]):
                que.popleft()

            
            if (r-l+1) >= k:
                result.append(nums[que[0]])
                l = l+1
            
        return result