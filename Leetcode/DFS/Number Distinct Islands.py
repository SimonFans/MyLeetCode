'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.
形状相同的岛视为一个岛

Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1

1 1 0 0 0
1 1 0 0 0
0 0 0 1 1
0 0 0 1 1

Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3

1 1 0 1 1
1 0 0 0 0
0 0 0 0 1
1 1 0 1 1
'''

解法： dfs + backtracking (记录direction然后比较)

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # How to determine how many of these islands have a unique shape
        # use dfs to make a list of islands, where each island is a list of coordinates

        def dfs(row, col, direction):
            nonlocal path
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
                return
            if (row, col) in seen:
                return
            seen.add((row, col))
            # path.append(direction)
            path += direction
            # right
            dfs(row, col+1, 'R')
            # down
            dfs(row+1, col, 'D')
            # left
            dfs(row, col-1, 'L')
            # up
            dfs(row-1, col, 'U')
            # For backtracking because it may get same path value but with different shapes
            path += 'E'

        seen = set()
        unique_islands = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # path = []
                path = ''
                dfs(row, col, 'S')
                if path:
                    # unique_islands.add(tuple(path))
                    unique_islands.add(path)
        return len(unique_islands)

# Time: O(M*N) row*col
# Space: O(M*N)
