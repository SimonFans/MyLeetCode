'''
The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.

For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.
Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums.
Since the answer may be large, return it modulo 10**9 + 7.

Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.

Input: nums = [3,1,5,6,4,2]
Output: 60
Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
4 * (5+6+4) = 4 * 15 = 60.
'''

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        # method: Monotonic Stack
        '''
        example: [3,1,5,6,4,2]
  example_index:  0 1 2 3 4 5
        preSum: [0,3,4,9,15,19,21]
        index:   0 1 2 3 4  5   6
        '''
        stack = []
        preSum = [0]
        res = 0
        for num in nums:
            preSum.append(preSum[-1] + num)
        # 目的是要单调递增，如果遇到递减数，stack pop，每次计算结果，直到找到比当前i所对应的值小或者等于的，最后更新index
        for i, num in enumerate(nums):
            new_start = i
            # 遇到比前一个数小的，也就是递减的情况发生
            while stack and stack[-1][1] > num:
                start, val = stack.pop()
                total_sum = preSum[i] - preSum[start]
                res = max(res, total_sum * val)
                new_start = start
            stack.append((new_start,num))
        for start, val in stack:
            total_sum = preSum[len(nums)] - preSum[start]
            res = max(res, total_sum*val)
        return res%(10**9+7)

# Time: O(N)
# Space: O(N)
