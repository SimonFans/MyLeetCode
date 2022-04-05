Given an integer array nums that may contain duplicates,
return all possible subsets (the power set).
The solution set must not contain duplicate subsets.
Return the solution in any order.

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        Backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again.
        example:
        [1,   2,    2]  don't want [1,2] and [1,2], so add if i> start and nums[i] == nums[i-1]
            start   i
        '''
        def backtrack(start, curr):
            ans.append(curr)
            # i -> 0,1,2
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                backtrack(i+1, curr + [nums[i]])
        ans = []
        nums.sort()
        backtrack(0,[])
        return ans
