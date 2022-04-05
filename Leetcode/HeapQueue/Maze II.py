'''
Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: 12
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
The length of the path is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
'''

思路：minHeap: (dist, start, end).
将起点和距离0加入minHeap. while当minHeap不为空，heapPOP最近的距离，起点和终点。
遍历四个方向，用另一个while去看这个方向一直走下去可不可以，一些限定条件比如边界，是不是遇到block，走到尽头后将尽头起点和终点，距离存入一个字典。
之后如果遇到走到相同的位置或者第一次走到这个位置，如果从别的地方走到这里更小，则更新字典的距离。最后压入minHeap.

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # row, col of maze
        row, col = len(maze), len(maze[0])
        # use heapq to extract the (x,y) with the minimum distance
        heap = []
        # 将起始点加入堆 => (距离，x, y)
        heapq.heappush(heap, (0, start[0], start[1]))
        # 记录走到当前位置的最小距离
        visited = {(start[0], start[1]): 0}

        # 循环直到内部到达目的地，返回距离值
        while heap:
            dist, x, y = heapq.heappop(heap)
            # if reach to the destination
            if x == destination[0] and y == destination[1]:
                return dist
            # steps into four directions
            for _x, _y in ((-1,0),(1,0),(0,-1),(0,1)):
                _newX, _newY, step = x, y, 0
                # Not beyond the row, col edge and not the wall
                while 0 <= _newX + _x < row and 0 <= _newY + _y < col and maze[_newX + _x][_newY + _y] != 1:
                    _newX += _x
                    _newY += _y
                    step += 1
                if (_newX, _newY) not in visited or dist + step < visited[(_newX, _newY)]:
                    visited[(_newX, _newY)] = dist + step
                    heapq.heappush(heap, (dist + step, _newX, _newY))
        return -1
