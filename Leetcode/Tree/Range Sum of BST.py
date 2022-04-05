'''
           10
         5    15
       3   7     18
给定一个inclusive range[low, high]
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # BFS
        if not root:
            return 0
        q = deque([root])
        res = 0
        while q:
            node = q.popleft()
            if low <= node.val and node.val <= high:
                res += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res

        # DFS
        def helper(node):
            if not node:
                return
            if low <= node.val <= high:
                self.ans += node.val
            if node.val > low:
                helper(node.left)
            if node.val < high:
                helper(node.right)
        self.ans = 0
        helper(root)
        return self.ans

        # time: O(N) space: O(N)
