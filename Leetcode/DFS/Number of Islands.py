'''
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

========================
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        '''
        1 means island
        0 means water
        '''
        # If matrix is empty, then return #of islands is 0
        if not grid:
            return 0
        # Initialize a counter
        count=0
        # Iterate through rows and columns in the matrix
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If current position is island, then call depth first search (recursion function)
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    count+=1
                    # if you want to see what's happened in the matrix, uncomment below print
                    #print(grid)
        return count

    def dfs(self,grid,i,j):
        # If any of below conditions is true, then do nothing just return
        # Else mark current postion as '#', and search the other four directions
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1':
            return
        grid[i][j]='#'
        # search down
        self.dfs(grid,i+1,j)
        # search up
        self.dfs(grid,i-1,j)
        # search right
        self.dfs(grid,i,j+1)
        # search left
        self.dfs(grid,i,j-1)


Time: O(M*N) where M is the number of rows, and N is the number of columns
Space: The worst case is O(M*N). Because grid map is filled with lands where DFS goes by M*N steps
