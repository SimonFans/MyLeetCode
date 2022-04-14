'''
Input: s = "(()"
Output: 2

Input: s = ")()())"
Output: 4
'''
分析：从左向右遍历整个string，遇到左括号压下标进stack。定义一个start指针在index -1位置
     遇到右括号，(1)当前stack是空，即没有左括号，直接将start指针移到当前右括号位置
     （2）当前stack不为空，则从stack中pop出左括号，
      （2.1）如果pop后stack为空，则当前右括号位置减去start指针位置
      （2.2）如果pop后stack不为空，即还有左括号，则当前右括号位置减去stack中最后一个左括号的位置

Time: O(N), O(N)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        res = 0
        # start = -1 for case: '()'
        start = -1
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                # is ')'
                if len(stack) == 0:
                    start = i
                else:
                    stack.pop()
                    if len(stack) == 0:
                        res = max(res,i - start)
                    else:
                        res = max(res,i - stack[-1])
        return res
