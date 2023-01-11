'''
Input: grid = [[1,3,1],
               [1,5,1],
               [4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    continue
                elif row == 0:
                    grid[row][col] = grid[row][col-1] + grid[row][col] 
                elif col == 0:
                    grid[row][col] = grid[row-1][col] + grid[row][col]
                else:
                    grid[row][col] = min(grid[row-1][col], grid[row][col-1]) + grid[row][col]
        return grid[row][col]

# Time: O(rows*cols)
# Space: O(1) no extra space
