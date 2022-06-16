class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def isMatSame(mat, target):
            for i in range(len(mat)):
                for j in range(len(mat)):
                    if mat[i][j] != target[i][j]:
                        return False
            
            return True
        
        
        def rotate(mat):
            result = [[1] * len(mat) for i in range(len(mat))]
               
            for i in range(len(mat)):
                for j in range(len(mat)):
                    column = len(mat) - i - 1
                    row = j
                    result[row][column] = mat[i][j]
            
            return result
        
        rotateM = mat
        for i in range(4):
            
            if isMatSame(rotateM, target):
                return True
            
            rotateM = rotate(rotateM)
            
            
        return False
        