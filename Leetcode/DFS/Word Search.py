'''
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
'''

Time: O(N*3^L), N is the number of cells in the board. L is the length of word to be matched.
Space: O(L): recursion call, call stack

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, suffix):
            # termination on suffix is empty
            if len(suffix) == 0:
                return True
            # beyond the edge or current char != target
            if row < 0 or col < 0 or row == rows or col == cols or board[row][col] != suffix[0]:
                return False

            board[row][col] = '#'
            # four directions to search
            for r, c in [(0,1), (-1, 0), (0,-1), (1,0)]:
                if backtrack(row+r, col+c, suffix[1:]):
                    return True
            # Revert the making
            # if C 右边的E也是C， 这时候要backfill
            board[row][col] = suffix[0]
            return False

        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, word):
                    return True
        return False
