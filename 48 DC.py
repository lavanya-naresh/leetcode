from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        
        for currRow in range(row):
            for currCol in range(currRow, col):
                matrix[currRow][currCol], matrix[currCol][currRow] = matrix[currCol][currRow], matrix[currRow][currCol]
        
        for currRow in range(row):
            matrix[currRow].reverse()
        
        return matrix