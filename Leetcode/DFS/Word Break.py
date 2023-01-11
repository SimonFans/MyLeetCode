'''
Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # edge case: if string is empty, then return False
        def dfs(s, word_set, memo):
            # 记忆中找到之前匹配的结果,加速返回
            if s in memo:
                return memo[s]
            # 如果此时字符串为空，说明都匹配上了，直接出口条件返回True
            if not s:
                return True
            for word in word_set:
                if s[:len(word)] != word:
                    continue
                # 当前位置之前的单词匹配其中一个目标单词的，所以可以将这个单词存入memo中方便以后快速查询
                memo[word] = True
                # 访问之后的单词
                if dfs(s[len(word):], word_set, memo):
                    return True
            memo[s] = False
            return False
        # main function
        if not s:
            return False
        word_set = set(wordDict)
        memo = defaultdict(bool)
        return dfs(s, word_set, memo)

'''
Time: O(N^3)
Using memoization, we guarantee that T(N-2) will happen only once and for all other lengths of N.
T(N) = N(N-1) / 2 => in Big-O: O(N^2)
Each time we compute the answer for a substring,
we have to build up to that substring which is O(N).
In python, string is immutable.
This means that even if you have something like string_build += new_character in a for-loop,
you are rebuilding the string from scratch every time

Space: O(N)
The depth of recursion tree can go up to n
'''
