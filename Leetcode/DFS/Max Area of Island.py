'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,1,1,0,1,0,0,0,0,0,0,0,0],
               [0,1,0,0,1,1,0,0,1,0,1,0,0],
               [0,1,0,0,1,1,0,0,1,1,1,0,0],
               [0,0,0,0,0,0,0,0,0,0,1,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def helper(i, j):
            '''
            Return condition:
            1. if out of boundary
            2. if the position is water
            3. if the position has been visited
            '''
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != 1 or (i,j) in seen:
                return 0
            seen.add((i, j))
            return 1 + helper(i+1, j) + helper(i-1, j) + helper(i, j-1) + helper(i, j+1)
        rows, cols = len(grid), len(grid[0])
        ans = 0
        seen = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans = max(ans, helper(i,j))
        return ans

# Time: O(R*C) where R is the number of rows and C is the number of columns
# Space: O(R*C)
