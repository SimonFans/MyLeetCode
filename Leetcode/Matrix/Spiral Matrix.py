'''
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
螺旋打印
1 2 3
4 5 6
7 8 9
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, cols = len(matrix), len(matrix[0])
        up, left = 0, 0
        right = cols -1
        down = rows - 1
        while len(result) < rows * cols:
            # from left to right, up is boundary
            for col in range(left, right + 1):
                result.append(matrix[up][col])
            # from up to down, right is boundary
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])
            # from right to left, down is boundary
            if up != down:
                for col in range(right-1, left-1, -1):
                    result.append(matrix[down][col])
            # from down to up, left is boundary
            if left != right:
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])
            up += 1
            down -= 1
            left += 1
            right -= 1
        return result

# Time: O(M*N)
# Space: O(1) but I feel like it's O(M*N)
