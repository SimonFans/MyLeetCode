'''
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Edge Case
        if len(s) < len(p):
            return []

        ans = []
        window_size = len(p)
        p_cnt = [0] * 26
        s_cnt = [0] * 26
        # initialize the target p
        for ch in p:
            p_cnt[ord(ch) - ord('a')] += 1
        # Then iterate the source s
        left, right = 0, 0
        while right < len(s):
            s_cnt[ord(s[right]) - ord('a')] += 1
            if right - left + 1 >= window_size:
                if s_cnt == p_cnt:
                    ans.append(left)
                s_cnt[ord(s[left]) - ord('a')] -= 1
                left += 1
            right += 1
        return ans
# Time: O(Ns) the length of string s
# Space: O(26) ~ O(1)
