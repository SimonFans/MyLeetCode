'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

2 1 1    2 2 1   2 2 2   2 2 2   2 2 2
1 1 0    2 1 0   2 2 0   2 2 0   2 2 0
0 1 1    0 1 1   0 1 1   0 2 1   0 2 2

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        queue = collections.deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_count += 1
                elif grid[row][col] == 2:
                    queue.append((row, col, 0))
        seen = set()
        while queue:
            x, y, res = queue.popleft()
            dirs = {(x-1,y), (x+1,y), (x, y-1), (x, y+1)}
            for nx, ny in dirs:
                # Got a fresh orange
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in seen and grid[nx][ny] == 1:
                    seen.add((nx, ny))
                    fresh_count -= 1
                    if fresh_count == 0:
                        return res + 1
                    queue.append((nx, ny, res + 1))
        # edge case: [[0,2]], if no fresh orange in the grid, which means there's value 1
        # then return 0 means 0 minutes needed
        return 0 if fresh_count == 0 else -1

# Time complexity: O(n),
# space complexity: O(n),
# where n is the total number of cells.
