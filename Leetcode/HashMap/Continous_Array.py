'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        count : index
        if meet 0, count -= 1
        if meet 1, count += 1

        '''
        hashMap = {0: -1}
        count = 0
        max_len = 0
        for i, num in enumerate(nums):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            # count值代表多少个0. -1多出来多少个0， 1是少了多少了0
            if count in hashMap:
                max_len = max(max_len, i - hashMap[count])
            else:
                hashMap[count] = i
        return max_len
