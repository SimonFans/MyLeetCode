'''
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
'''

# stack time: O(m+n), space: O(m+n)
class Solution(object):
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)

# note skip value time: O(m+n), space: O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        skipS = skipT = 0
        while True:
            while i >= 0 and (skipS or s[i] == '#'):
                skipS += 1 if s[i] == '#' else -1
                i -= 1
            while j >= 0 and (skipT or t[j] == '#'):
                skipT += 1 if t[j] == '#' else -1
                j -= 1
            if not (i >= 0 and j >= 0 and s[i] == t[j]):
                return i == j == -1
            i, j = i - 1, j - 1
