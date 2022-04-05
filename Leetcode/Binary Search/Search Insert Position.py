'''
Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 7
Output: 4
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # edge case when target > max(nums) return length of the list
        if target > max(nums):
            return len(nums)
        # binary search
        while left + 1 < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        # keep two at the end. discuss the target location at possible x postion => x A x B
        if target <= nums[left]:
            return left
        else:
            return right
O(logN) O(1)
