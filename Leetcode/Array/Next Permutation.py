'''
Input: nums = [1,2,3]
Output: [1,3,2]

Input: nums = [3,2,1]
Output: [1,2,3]

Input: nums = [1,1,5]
Output: [1,5,1]

Input: nums = [6 8 5 4]
Output: [8,4,5,6]
'''
思路：从后向前找到第一个峰值，记录下它之前的index比如i，用于之后交换。此时峰值后的数字都是降序排列
     再一次从后往前找，每一次与i位置的值比较，记录下标j where nums[j]>= nums[i]
     交换
     此时i之后的数字仍然是降序排列，所以需要变成升序排列,可以同样使用交换的方法
     example:
     6 8 5 4     6 8 5 4   8 6 5 4   8 4 5 6
     i           i j         i

Time: O(n) , Space: O(1)

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        # Turn the rest of array from in desceding order to ascending order
        def reverse(start):
            i, k = start, len(nums) - 1
            while i < k:
                swap(i,k)
                i+=1
                k-=1
        # 程序开始位置， 定位在倒数第二个数字
        i = len(nums) - 2
        # i >= 0 如果初始数组是降序排列，则i最后会等于-1
        while i >=0 and nums[i] >= nums[i+1]:
            i -= 1
        if i>=0:
            j = len(nums) -1
            while nums[j] <= nums[i]:
                j -=1
            swap(i,j)
        reverse(i+1)
