'''
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''

思路： 此题要找出出现在数组中频率最大的K个数字。借用字典Counter去统计每个数字出现的个数，之后遍历字典造一个(value*-1, key)的形式放入heap.
这样做是因为乘完-1之后，最大的frequency就变成了最小的。为之后的while循化做基础。while循环会一直从heap中pop，知道取到的数字=k

from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        num_freq = Counter(nums)
        for key, val in num_freq.items():
            heapq.heappush(heap, (val*-1,key))
        while len(res) < k:
            _, x = heapq.heappop(heap)
            res.append(x)
        return res
