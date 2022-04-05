'''
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
'''
中心对称法

'''
Thoughts:
a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center.
If n is the length of the string, then there's only 2n - 1 such centers.
example:
s = 'abc'
so the center will be a, b, c, ab, and bc which is 2n-1 = 5
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s,left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        longest = ""
        for i in range(len(s)):
            odd_str = isPalindrome(s,i,i)
            if len(odd_str) > len(longest):
                longest = odd_str
            even_str =isPalindrome(s,i,i+1)
            if len(even_str) >len(longest):
                longest = even_str
        return longest

# time: O(N^2) 
# space: O(1)
