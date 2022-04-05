'''
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
'''

思路： 因为要找到K个最大的数字，可以先把K个数字放入heap.因为heap中第一个数字永远都是最小的，接下来从K遍历到最后一个数字。
如果发现遍历到的数字大于heap[0], 则heap pop一次，即拿出最小的数字，之后再将当前的数字push到heap中去。最后返回heap[0]即答案

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = [nums[i] for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
        return heap[0]
