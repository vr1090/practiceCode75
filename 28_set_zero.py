class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        
        copy = [[-1] * cols for i in range(rows)]
        
        # create a function, for change copy in col and row
        def setZeroInCopy(i, j):
            for z in range(rows):
                copy[z][j] = 0
            
            for z in range(cols):
                copy[i][z] = 0
        
        # iterate, to generate the copy column
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    setZeroInCopy(i,j)
        
        
        #copy the copy to the matrix
        for i in range(rows):
            for j in range(cols):
                if copy[i][j] == 0:
                    matrix[i][j] = 0
            