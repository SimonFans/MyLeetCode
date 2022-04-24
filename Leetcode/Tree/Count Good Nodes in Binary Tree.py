'''
Given a binary tree root, a node X in the tree is named good
if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
        3
     1    4
   3  N  1   5

Good node will be 3,3,4 and 5, so return 4 is the answer.
Because path candidates can be:
3, root node 3 is always the answer, because there's only one node
3->1 , 1 is not good node because current path max value is 3. 1 is < 3
3->1->3, the last 3 is good node because current path max value is 3, 3 >= 3
...
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            nonlocal ans
            if node.val >= max_so_far:
                ans += 1
            if node.left:
                dfs(node.left, max(node.val, max_so_far))
            if node.right:
                dfs(node.right, max(node.val,max_so_far))
        ans = 0
        dfs(root, float('-Inf'))
        return ans

# Time: O(N)
# Because we visited every node exactly once
# Space: O(N) Call stack can be as large as the height of tree

# BFS
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        queue = deque([(root, float('-Inf'))])
        while queue:
            node, max_so_far = queue.popleft()
            if node.val >= max_so_far:
                ans += 1
            if node.left:
                queue.append((node.left, max(node.val, max_so_far)))
            if node.right:
                queue.append((node.right, max(node.val, max_so_far)))
        return ans

# Time: O(N)
# Because we visited every node exactly once
# Space: O(N)
