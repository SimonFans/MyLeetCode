'''
Given an integer array nums,
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
给一个整数数组，问子数组连续和最大值是多少

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

          -2   1  -3  4 -1  2  1  -5  4
curr      -2   1  -3  4 -1  2  1  -5  4
curr_sum  -2   1  -2  4  3  5  6   1  5
max_sum   -2   1   1  4  4  5  6   6  6 => answer
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray, max_subarray = nums[0], nums[0]
        for num in nums[1:]:
            current_subarray = max(num, num + current_subarray)
            max_subarray = max(max_subarray, current_subarray)
        return max_subarray
