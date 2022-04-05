'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa"
'''

# time: O(N^2) The number of possbile palindrome center is 2N - 1.
#       Each center can expand to the length of the string, so the total time spent is N*(2N-1) ~ N^2
# space: O(1) we don't need to allocate any extra space

class Solution:

    def countSubstrings(self, s: str) -> int:
        if len(s)==0:
            return 0
        size=len(s)
        result=0
        for i in range(size):
            # odd length, single character center
            result += self.helper(s,i,i)
            # even length, consecutive characters center
            result += self.helper(s,i,i+1)
        return result

    def helper(self, s, start, end):
        res = 0
        while start >= 0 and end < len(s) and s[start]==s[end]:
            start-=1
            end+=1
            res+=1
        return res
