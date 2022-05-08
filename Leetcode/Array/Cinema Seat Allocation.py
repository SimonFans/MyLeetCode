'''
      1 2 3 || 4 5 6 7 || 8 9 10
Row1:   x x               x
Row2:              x
Row3: x                       x
Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output: 2
Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4
'''

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # 连续4个人坐在一起，有通道的时候，必须两边各有两个人
        # 一行10个座位，最多4个连排的可能性是2个。N行最多连排的可能性是2*N
        # 两种方案：(1) 2,3,4,5 and 6,7,8,9. (2) 4,5,6,7
        seats = collections.defaultdict(set)
        total_possibility = 2 * n
        for i, j in reservedSeats:
            if j in (2,3,4,5):
                seats[i].add(0)
            if j in (4,5,6,7):
                seats[i].add(1)
            if j in (6,7,8,9):
                seats[i].add(2)
        # defaultdict(<class 'set'>, {1: {0, 2}, 2: {1, 2}})
        for i in seats:
            # 没有连续四个的位置
            if len(seats[i]) == 3:
                total_possibility -= 2
            # 还有一个四人的位置
            else:
                total_possibility -= 1
        return total_possibility
