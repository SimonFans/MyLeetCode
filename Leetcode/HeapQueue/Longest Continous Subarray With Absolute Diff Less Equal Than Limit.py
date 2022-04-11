'''
Input: nums = [8,2,4,7], limit = 4
Output: 2

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
'''

import collections
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq = collections.deque()
        minq = collections.deque()
        i = 0
        for num in nums:
            # The first number is always the largest
            while len(maxq) and maxq[-1] < num:
                maxq.pop()
             # The first number is always the minimum
            while len(minq) and minq[-1] > num:
                minq.pop()
            maxq.append(num)
            minq.append(num)
            if maxq[0] - minq[0] > limit:
                if maxq[0] == nums[i]:
                    maxq.popleft()
                if minq[0] == nums[i]:
                    minq.popleft()
                i += 1
        return len(nums) - i

# Time: O(N)
# Space: O(N)

'''
Heap solution
'''

def longestSubarray(self, A, limit):
        maxq, minq = [], []
        res = i = 0
        for j, a in enumerate(A):
            heapq.heappush(maxq, [-a, j])
            heapq.heappush(minq, [a, j])
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i: heapq.heappop(maxq)
                while minq[0][1] < i: heapq.heappop(minq)
            res = max(res, j - i + 1)
        return res

# Time: O(NLogN)
# Space: O(N)
