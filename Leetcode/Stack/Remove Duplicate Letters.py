'''
Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Input: s = "bcabc"
Output: "abc"

Input: s = "cbacdcbc"
Output: "acdb"
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        # record the last position a character stays at
        last_occurence = {c:i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c not in seen:
                '''
                Go with while loop if
                1. character exists in stack
                2. current character ASCII value < top elements in the stack
                3. top element in stack has more after the current index
                '''
                while stack and stack[-1] > c and i < last_occurence[stack[-1]]:
                    top = stack.pop()
                    seen.discard(top)
                seen.add(c)
                stack.append(c)
        return ''.join(stack)
'''
Time complexity : Inner while loop is still O(N) because the inner while loop
is bounded by the total number of elements added to the stack (each time it fires an element goes)

Space complexity: O(1) not O(N) because seen is a set only contain unique elements,
you can only add to stack if an element has not been seen. So stack also only
consists of unique elements
'''
