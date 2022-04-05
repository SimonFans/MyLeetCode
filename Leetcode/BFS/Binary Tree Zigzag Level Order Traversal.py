'''
Input: root = [3,9,20,null,null,15,7]

       3
     9   20
        15  7
=============
Output: [[3],[20,9],[15,7]]
'''
思路： 需要一个层数计数器，当遇到偶数时，直接加level list。遇到奇数时，加level[::-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = collections.deque()
        res=[]
        if root==None:
            return res
        queue.append(root)
        l=0

        while queue:
            level=[]
            for i in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if l%2==1:
                res.append(level[::-1])
            else:
                res.append(level)
            l+=1
        return res
