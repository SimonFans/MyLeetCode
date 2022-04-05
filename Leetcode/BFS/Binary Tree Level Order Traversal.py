'''
Given the root of a binary tree,
return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
    3
  9   20
    15  7
==========
[[3], [9,20], [15,7]]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # edge case, if root is null then return []
        if not root:
            return []
        # declare a list to store the result
        res = []
        # bfs
        queue = deque([root])
        while queue:
            # this list is used to store values in each level
            level = []
            # Loop through all node in the current level
            for _ in range(len(queue)):
                # pop nodes in the current level
                node = queue.popleft()
                # store the value into the temp list
                level.append(node.val)
                # if current node has left child
                if node.left:
                    queue.append(node.left)
                # if current node has right child
                if node.right:
                    queue.append(node.right)
            # append results in each level into the final list
            res.append(level)
        return res
