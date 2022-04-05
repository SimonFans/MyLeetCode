'''
Given a sorted integer array arr, two integers k and x,
return the k closest integers to x in the array.
The result should also be sorted in ascending order.
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
'''

思路：遍历整个数组，只保留长度为K的heap。发现距离与目标值绝对值更近的，
heap pop and push较近距离的数到heap

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) < k:
            return []
        heap = []
        for val in arr:
            dist = abs(val - x)
            if len(heap) < k:
                heappush(heap, (-1 * dist, val))
            else:
                if -1 * heap[0][0] > dist:
                    heappop(heap)
                    heappush(heap, (-1 * dist, val))
        return sorted([val for _, val in heap])
