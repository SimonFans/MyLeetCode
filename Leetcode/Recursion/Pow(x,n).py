'''
Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0: return 1.0/self.myPow(x,-n)
        half = self.myPow(x, n//2)
        if n %2 == 0:
            return half * half
        else:
            return half * half * x

'''
Take 2^4 as an example

half = (2, 4//2)
half = (2, 2//2)
half = (2, 1//2)

for each returned half, depends on nominator value example: (1//2) => 1, return result

'''
