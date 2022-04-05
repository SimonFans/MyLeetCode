'''
Input: root = [1,2,3,null,5,null,4]
       1
   2      3
      5      4
Output: [1,3,4]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        思路： bfs + 循环每一层，当index==最后一个value index时，即为最右边的value，加入返回list

        '''
        if not root:
            return []
        queue = deque([root])
        # return list
        right_side = []
        while queue:
            # how many nodes in each level
            current_level_length = len(queue)
            # Iterate through the current level values
            for i in range(current_level_length):
                node = queue.popleft()
                # if current node is the rightmost, then append to return list
                if i == current_level_length - 1:
                    right_side.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return right_side
