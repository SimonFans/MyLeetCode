# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val, q_val = p.val, q.val
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if p_val < cur.val and q_val < cur.val:
                queue.append(cur.left)
            elif p_val > cur.val and q_val > cur.val:
                queue.append(cur.right)
            else:
                return cur


        '''
        Due to it's a binary search tree, left node val < root node val, right node val > root node val
        Find the split point and return
        Solution: bfs
        '''
