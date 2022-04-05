'''
Given a 2D matrix matrix, handle multiple queries of the following types:

Update the value of a cell in matrix.
Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1)
and lower right corner (row2, col2).

Input
["NumMatrix", "sumRegion", "update", "sumRegion"]

[[[[3, 0, 1, 4, 2],
   [5, 6, 3, 2, 1],
   [1, 2, 0, 1, 5],
   [4, 1, 0, 1, 7],
   [1, 0, 3, 0, 5]]
],

[2, 1, 4, 3], [3, 2, 2], [2, 1, 4, 3]]

Output
[null, 8, null, 10]
'''

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # 遍历每一行，做presum。比如：[3,1,0,4,2] => [3,4,4,8,10]
        for row in matrix:
            for col in range(1, len(matrix[0])):
                row[col] += row[col-1]
        self.matrix = matrix
        print(matrix)

    def update(self, row: int, col: int, val: int) -> None:
        # 先根据row, col拿到当前对应的累加值
        original_val = self.matrix[row][col]
        # 如果不是第一列，则先用当前的累加值减去之前的累加值得到当前原始值
        if col != 0:
            original_val -= self.matrix[row][col-1]
        # 计算一下更新的值与原始值差了多少
        diff = original_val - val
        # 将变化的值加入到当前的累加值中去
        for j in range(col, len(self.matrix[0])):
            self.matrix[row][j] -= diff

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sum = 0
        for r in range(row1, row2+1):
            _sum += self.matrix[r][col2]
            # 第一个column位置不是第一列时，每行最终结果都要减去前一列的值，因为不算之前的累加和
            if col1 != 0:
                _sum -= self.matrix[r][col1 - 1]
        return _sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
