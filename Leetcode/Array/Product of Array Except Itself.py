'''
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

example 1 idea:
1           2       3        4
1           1      1*2      1*2*3  ->
1*2*3*4   1*3*4    1*2*4     1     <-

'''



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res=[1]*len(nums)

        left=1
        for i in range(len(nums)-1):
            left*=nums[i]
            res[i+1]=left
        right=1
        for i in range(len(nums)-1,0,-1):
            right*=nums[i]
            res[i-1]*=right
        return res

# time: O(N)
# space: O(N)
