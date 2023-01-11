'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
'''

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        (0,0) (0,1) (0,2)
        (1,0) (1,1) (1,2)
        (2,0) (2,1) (2,2)
        """
        rows = len(board)
        cols = len(board[0])
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        live_neighbor = 0
        for row in range(rows):
            for col in range(cols):
                live_neighbor = self.count_live_neighbor(board, directions, row, col)
                # rule 1 & rule 3 the cell was alive but now is dead
                if board[row][col] == 1 and (live_neighbor < 2 or live_neighbor > 3):
                    board[row][col] = -1
                # rule 4 the cell was dead but now is alive
                if board[row][col] == 0 and live_neighbor == 3:
                    board[row][col] = 2
        # Lastly, if number is > 0 then 1 else 0
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0

    def count_live_neighbor(self, board, directions, row, col):
        live_neighbor = 0
        for x, y in directions:
            nx = x + row
            ny = y + col
            if (nx >=0 and nx < len(board)) and (ny>=0 and ny < len(board[0])) and abs(board[nx][ny]) == 1:
                live_neighbor += 1
        return live_neighbor

# Time: O(M*N) rows*cols
# Space: O(1) no extra space needed, modify board in-place 
