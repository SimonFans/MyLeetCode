'''
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "pwwkew"
Output: 3
'''

Time: O(n), Space: O(n)

思路： 建一个hashMap保存每个字符的个数: {'char': count}。建立左指针和右指针。右指针从左到右遍历string，
      一个while循环如果通过字典发现当前字符的个数大于1，则向右移动最左边的指针，
      并且对左指针指向的字符在字典中进行减1操作，直到右指针指向的字符不大于一个。
      最后注意要记录最大长度，即右指针减去左指针+1的距离

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0,0
        maxLen = 0
        hashMap = collections.defaultdict(int)
        for right in range(len(s)):
            hashMap[s[right]] += 1
            while hashMap[s[right]] > 1:
                hashMap[s[left]] -= 1
                left += 1
            maxLen = max(maxLen, right-left+1)
        return maxLen
