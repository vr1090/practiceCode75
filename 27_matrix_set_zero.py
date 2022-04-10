class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        
        copy = [[-1] * cols for i in range(rows)]
        
        
        def updateCopy(r,c):
            for i in range(rows):
                copy[i][c] = 0
            
            for i in range(cols):
                copy[r][i] = 0
                
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    updateCopy(i,j)
        
        
        for i in range(rows):
            for j in range(cols):
                if copy[i][j]== 0:
                    matrix[i][j] = 0
        