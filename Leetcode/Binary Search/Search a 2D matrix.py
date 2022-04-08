'''
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''

'''
此题将二维变1维。 index从0到 m*n - 1.
横轴：mid // 列数n
列轴: mid % 列数n
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n  = len(matrix), len(matrix[0])
        left, right = 0, m*n - 1
        while left + 1  < right:
            mid = (left + right)//2
            if matrix[mid//n][mid%n] < target:
                left = mid
            else:
                right = mid
        if matrix[left//n][left%n] == target or matrix[right//n][right%n] == target:
            return True
        return False

Time: O(log(m*n))
Space: O(1)
