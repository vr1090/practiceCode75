class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        blocks = collections.defaultdict(set)
        
        for i in range(len(board)):
            for j in range( len(board)):
                point = board[i][j]
                if point == ".":
                    continue
                
                if point in rows[i] or point in cols[j] or point in blocks[ (i//3, j//3) ]:
                    return False
                
                rows[i].add(point)
                cols[j].add(point)
                blocks[(i//3, j//3)].add(point)
        
        return True