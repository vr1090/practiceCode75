class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) -1
        top, bottom = 0, len(matrix) -1
        
        
        while left < right and top < bottom :
            for i in range( right-left):
                temp = matrix[top][left+i]
                matrix[top][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top+i][right]
                matrix[top+i][right] = temp
            
        
            left = left + 1
            right = right - 1
            top = top + 1
            bottom = bottom -1
            
                