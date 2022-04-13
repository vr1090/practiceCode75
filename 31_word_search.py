class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lenR = len(board)
        lenC = len(board[0])
        visited = set()
        
        def dfs(r,c, i):
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r >= lenR or c >= lenC:
                return False
            
            if board[r][c] != word[i]:
                return False
            
            
            if (r,c) in visited:
                return False
            
            moves = [[1,0], [-1,0], [0,1],[0,-1]]
            
            visited.add((r,c))
            result = False
            for addR, addC in moves:
                result = result or dfs(r+addR,c+addC, i+1)
            
            visited.remove( (r,c))
            
            return result
            
        
        for i in range(lenR):
            for j in range(lenC):
                if dfs(i,j,0):
                    return True
        
        return False