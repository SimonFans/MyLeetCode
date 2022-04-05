'''
Input: x = 4
Output: 2

Input: x = 8
Output: 2

'''

class Solution:
    def mySqrt(self, x: int) -> int:

        if x<2:
            return x

        left,right=1,x//2

        while left<=right:
            
            mid=left+(right-left)//2

            if mid**2>x:
                right=mid-1
            else:
                left=mid+1

        return left-1   # when left>right 越界，取left-1.
