'''
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        steps:
        1. create a set to record the index (if the stack is empty, meet ')', add to set)
        2. create a stack to record '('
           if there's a ')', pop the stack, stack may have redundent '(' (need to remove)
        3. union set with set(stack) which are all indices going to remove.
        4. rebuild the string using a for loop
        '''
        # Time: O(n), n is the length of the input string
        # Space: O(n) n is the length of the input string

        index_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in '()':
                continue
            elif c == '(':
                stack.append(i)
            elif not stack:
                index_to_remove.add(i)
            else:
                stack.pop()

        all_index_to_remove = index_to_remove.union(set(stack))

        res =''

        for i, c in enumerate(s):
            if i not in all_index_to_remove:
                res += c
        return res
