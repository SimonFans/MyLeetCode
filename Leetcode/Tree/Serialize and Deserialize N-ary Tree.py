"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        # serialized result => "1[2[]3[6[]7[11[14[]]]]4[8[12[]]]5[9[13[]]10[]]"
        def dfs(node):
            if not node:
                return
            res.append(str(node.val)+"[")
            for child in node.children:
                if child:
                    dfs(child)
            res.append("]")

        res = []
        dfs(root)
        return "".join(res)

	'''
                   1
            2     3       4     5
                6   7     8    9  10
                  11 14   12   13
    '''
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        data = data.split("]")
        data.pop() # pop the extra "" at the end
        head = None
        stack = []
        for string in data:
            chars = string.split("[")
            for char in chars:
                if char != "":
                    if not head:
                        head = Node(int(char),[])
                        stack.append(head)
                    else:
                        node = Node(int(char), [])
                        stack[-1].children.append(node)
                        stack.append(node)
            stack.pop()
        return head

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Time complexity for both serialize and deserialize: O(n). Space complexity for both serialize and deserialize: O(n).
