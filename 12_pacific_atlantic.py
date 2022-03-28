def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    rows = len(heights)
    cols = len(heights[0])
    res = []
    visitedPac = set()
    visitedAtl = set()
    
    
    
    def dfs(r,c,sets,prev):
        if (r,c) in sets:
            return
        
        if r < 0 or c < 0 or r == rows or c == cols:
            return
        
        if heights[r][c] < prev:
            return
        
        sets.add( (r,c) )
        
        dfs(r+1,c,sets, heights[r][c])
        dfs(r-1,c,sets, heights[r][c])
        dfs(r, c+1, sets, heights[r][c])
        dfs(r, c-1, sets, heights[r][c])
    
    for i in range(cols):
        dfs(0,i,visitedPac, heights[0][i])
        dfs(rows-1, i, visitedAtl, heights[rows-1][i])
        
    for i in range(rows):
        dfs(i,0,visitedPac,heights[i][0])
        dfs(i, cols-1, visitedAtl, heights[i][cols-1])
        
    
    for r in range(rows):
        for c in range(cols):
            if (r,c) in visitedPac and (r,c) in visitedAtl:
                res.append( (r,c))
        
    
    return res