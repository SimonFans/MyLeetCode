# Input: x = 2.10000, n = 3
# Output: 9.26100
#
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

def myPow(x,n):
    if n == 0: return 1
    if n < 0: return 1.0/myPow(x,-n)
    half = myPow(x,n//2)
    if n%2 ==0:
        return half * half
    else:
        return x * half * half

Time: O(logn)
Space: O(logn)
