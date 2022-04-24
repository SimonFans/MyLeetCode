'''
Given the root of a binary search tree and a target value,
return the value in the BST that is closest to the target.

Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Input: root = [1], target = 4.428571
Output: 1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#此题只要求返回最近的一个node
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def helper(node, target):
            nonlocal res, dist
            if not node:
                return
            helper(node.left, target)
            if abs(node.val - target) <= dist:
                dist = min(dist, abs(node.val-target))
                res = node.val
            helper(node.right, target)

        res = 0
        dist = float('Inf')
        # 利用了BST特点进行剪枝，排除掉一半的tree node
        if target <= root.val:
            root.right = None
        else:
            root.left = None
        helper(root, target)
        return res

# Time: O(max(Left tree height, Right tree height))
# Space: O(1)
