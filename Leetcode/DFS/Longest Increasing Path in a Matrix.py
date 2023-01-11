'''
Input: matrix = [[9,9,4],
                 [6,6,8],
                 [2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
'''

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(matrix, i, j, cache):
            if cache[i][j] != 0: return cache[i][j]
            for nx, ny in [(i-1,j),(i, j+1),(i+1, j),(i, j-1)]:
                if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] > matrix[i][j]:
                    cache[i][j] = max(cache[i][j], dfs(matrix, nx, ny, cache))
            #当前位置第一次走，如果之前走过，第一个if就返回了        
            cache[i][j] += 1
            return cache[i][j]

        row, col = len(matrix), len(matrix[0])
        # each value means at the current(x,y), the farest it can walk to
        cache = [[0] * col for _ in range(row)]
        ans = 0
        for i in range(row):
            for j in range(col):
                ans = max(ans, dfs(matrix, i, j, cache))
        return ans

# Time: O(M*N) with memorization
# Space: O(M*N)
