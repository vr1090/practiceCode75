class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lenRow = len(board)
        lenCol = len(board[0])
        
        visited = set()
        
        def dfs(r,c,i):
            
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r == lenRow or c == lenCol:
                return False
            

            if board[r][c] != word[i]:
                return False
            
            if (r,c) in visited:
                return False
            
            visited.add( (r,c) )
            
            result = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1)
            visited.remove( (r,c) )
            
            return result
        
        for r in range( lenRow):
            for c in range(lenCol):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        
        return False