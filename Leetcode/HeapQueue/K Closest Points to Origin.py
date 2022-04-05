'''
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
'''

思路：先将K个坐标点存入heap中，format为(负的<到原点的距离平方和>, <下标位置>)。从K开始遍历剩下的坐标点，如果当前坐标距离求负后比heap[0][0]大，
则代表找到一个离原点更近的。则heap pop & push当前相对更近的。最后通过heap中保存的下标，从points中返回对应的坐标值

Time: O(nlogk) add/remove from the heap takes O(logk)
Space: O(k)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDistance(point):
            return point[0]**2 + point[1]**2
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-getDistance(points[i]), i))
        for i in range(k, len(points)):
            if -getDistance(points[i]) > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-getDistance(points[i]), i))
        return [points[i]for _, i in heap]
