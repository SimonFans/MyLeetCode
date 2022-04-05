# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Serialization is the process of converting a data structure or object into a sequence of bits
so that it can be stored in a file or memory buffer, or transmitted across a network connection link
to be reconstructed later in the same or another computer environment.
'''

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue= deque([root])
        send_string_lst = []
        while queue:
            node = queue.popleft()
            send_string_lst.append(str(node.val) if node else '#')
            # if node is. '#' then no need to append to the deque
            if node:
                queue.append(node.left)
                queue.append(node.right)
        # string_lst => '1,2,3,#,#,4,5,#,#,#,#'
        return ','.join(send_string_lst)

    def deserialize(self, received_string):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        # received_string => '1,2,3,#,#,4,5,#,#,#,#'
        if not received_string:
            return None
        received_string_lst = received_string.split(',')
        # The first value should be the Tree root node
        root = TreeNode(int(received_string_lst[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if received_string_lst[index] is not '#':
                node.left = TreeNode(int(received_string_lst[index]))
                queue.append(node.left)
            index += 1
            if received_string_lst[index] is not '#':
                node.right = TreeNode(int(received_string_lst[index]))
                queue.append(node.right)
            index += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
