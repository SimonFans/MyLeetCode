class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        if len(s) < k:
            return s
        for c in s:
            # If stack is empty or previous stack character doesn't equal to the current character
            if not stack or stack[-1][0] != c:
                stack.append([c,1])
            # If previous stack character equals to current character, then check if it meets the threshold value
            # If yes, then pop the previous character
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            # List of strings -> string
        return ''.join([k*v for k, v in stack])
