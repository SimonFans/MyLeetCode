'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {'}':'{', ']':'[', ')':'('}
        stack = []
        for char in s:
            if char not in hashMap:
                stack.append(char)
            else:
                if not stack or stack[-1] != hashMap[char]:
                    return False
                stack.pop()
        return not stack
