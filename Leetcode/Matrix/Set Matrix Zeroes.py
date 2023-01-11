'''
Given an m x n integer matrix matrix,
if an element is 0, set its entire row and column to 0's.
You must do it in place.
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
1 1 1      1 0 1
1 0 1      0 0 0
1 1 1      1 0 1
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R=set()
        C=set()
        i=len(matrix)
        j=len(matrix[0])
        for r in range(i):
            for c in range(j):
                if matrix[r][c]==0:
                    R.add(r)
                    C.add(c)
        for r in range(i):
            for c in range(j):
                if r in R or c in C:
                    matrix[r][c]=0
Time: O(M*N)
Space: O(M+N)
