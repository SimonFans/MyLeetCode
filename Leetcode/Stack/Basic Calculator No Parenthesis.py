'''
Input: s = "3+2*2"
Output: 7

Input: s = " 3+5/2 "
Output: 5

Input: s = " 6 + 22*2 "
Output: 50
'''
class Solution:
    def calculate(self, s: str) -> int:
        # record 之前的结果
        stack=[]
        # 记录数字
        num=0
        # 开始默认operator为+
        pre_operator='+'
        for i, each in enumerate(s):
            # 如果当前为数字，可能多个数字则叠加
            if each.isdigit():
                num=10*num+int(each)
            # 如果当前非数字，根据之前的operator处理数字。注意不要丢掉最后一个数字的情况
            if i==len(s)-1 or each in "+-*/":
                if pre_operator=='+':
                    stack.append(num)
                elif pre_operator=='-':
                    stack.append(-num)
                elif pre_operator=='*':
                    stack.append(stack.pop()*num)
                elif pre_operator=='/':
                    # -3/2 = -1.5 need int here. rather than -3//2 = -2 (x)
                    stack.append(int(stack.pop()/num))
                # 每次遇到非数字，更新operator
                pre_operator=each
                # 每次遇到非数字，重置记录数字的变量为0
                num=0
        return sum(stack)

Time: O(N)  Space: O(N)
