'''
You are given a map of a server center,
represented as a m * n integer matrix grid,
where 1 means that on that cell there is a server and 0 means that it is no server.
Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server..
'''

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # store coordinates of all computers
        computers = []
        # store number of computers in a given row
        computers_per_row = [0] * rows
        # store number of computers in a given column
        computers_per_column = [0] * cols
        # return
        connected = 0
        # iterate through the grid, get the computer coordinates and count computers per row and column
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    computers.append((row,col))
                    computers_per_row[row] += 1
                    computers_per_column[col] += 1
        #Iterate through all computers
        for r, c in computers:
            # is there more than 1 computer in given row or column
            if computers_per_row[r] > 1 or computers_per_column[c] > 1
                connected += 1
        return connected

# Time: O(rows * cols)
# Space: O(rows* cols)
