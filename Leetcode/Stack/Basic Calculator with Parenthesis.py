'''
Input: s = "1 + 1"
Output: 2

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
'''

class Solution:
    def calculate(self, s: str) -> int:
        # final result
        res = 0
        # 1: '+', -1: '-'
        sign = 1
        # record number
        num = 0
        # need a stack to store previous value and sign
        stack = []

        for i, each in enumerate(s):
            if each.isdigit():
                num = num*10 + int(each)
            if each in '+-':
                # 将前面的数字和之前的运算符相乘然后存到最后的结果变量中
                res += sign*num
                # 因为现在在sign的位置，所以代表之前的number完事了，需要初始化
                num = 0
                # sign也要根据当前的sign更新
                sign = [-1, 1][each == '+']
            elif each == '(':
                # save previous value
                stack.append(res)
                # save sign value
                stack.append(sign)
                # new environment so need to reset num=0 and sign=1
                res = 0
                sign = 1
            elif each == ')':
                # close interval calculation first
                res += sign*num
                # pull the sign outside of the current '()'
                res *= stack.pop()
                # pull the previous total sum
                res += stack.pop()
                # reset num = 0
                num = 0
        # return don't forget to add the last number with its previous sign
        return res + sign*num

Time: O(N) Space: O(N)
