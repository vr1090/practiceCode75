class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        
        def dfs(pos, current):
            if sum(current) == target:
                res.append( current.copy() )
                return
            
            if pos >= len(candidates):
                return
            
            if sum(current) > target:
                return
            
            current.append(candidates[pos])
            dfs(pos, current)
            current.pop()
            dfs(pos+1, current)
        
        
        dfs(0, [])
        
        return res
        