class Solution:
   def setZeroes(self, matrix: List[List[int]]) -> None:
       """
       Do not return anything, modify matrix in-place instead.
       """
       first_row_zero = any(matrix[0][c] == 0 for c in range(len(matrix[0])))
       first_col_zero = any(matrix[r][0] == 0 for r in range(len(matrix)))
       
       for r in range(1, len(matrix)):
           for c in range(1, len(matrix[0])):
               if matrix[r][c] == 0:
                   matrix[r][0] = 0
                   matrix[0][c] = 0
       
       for r in range(1, len(matrix)):
           for c in range(1, len(matrix[0])):
               if matrix[r][0] == 0 or matrix[0][c] == 0:
                   matrix[r][c] = 0
       
       if first_row_zero:
           for i in range(len(matrix[0])):
               matrix[0][i] = 0
       
       if first_col_zero:
           for i in range(len(matrix)):
               matrix[i][0] = 0