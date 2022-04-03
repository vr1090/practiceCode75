class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        
        
        res.append(intervals[0])
        
        for i in range(1, len(intervals)):
            last = res[-1]
            cur = intervals[i]
            
            if last[1] >= cur[0]:
                res[-1] = [min(last[0], cur[0]), max(last[1], cur[1])]
            else:
                res.append(cur)
        
        
        
        return res