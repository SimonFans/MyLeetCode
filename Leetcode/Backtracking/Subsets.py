'''
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(start, curr):
            ans.append(curr)
            # i -> 0,1,2
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                helper(i+1, curr + [nums[i]])
        ans = []
        nums.sort()
        helper(0, [])
        return ans
