'''
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, tmp):
            if not nums:
                ans.append(list(tmp))
                return
            for i in range(len(nums)):
                # 当满足以下条件时，不对当前数字进行处理
                if i > 0 and nums[i-1] == nums[i]:
                    continue
                tmp.append(nums[i])
                helper(nums[:i]+nums[i+1:], tmp)
                tmp.pop()
        ans = []
        # 注意要开始时候sort
        nums.sort()
        helper(nums, [])
        return ans

# Time: O(N!)
# Space: O(N) ~ O(N!)
