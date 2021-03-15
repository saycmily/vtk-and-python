# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        q = deque([root])
        out = []
        while q:
            node = q.pop()
            out.append(str(node.val))
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return ','.join(out)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        def buildTree(pre_o, in_o):
            if not pre_o:
                return None
            mid = pre_o[0]
            i = in_o.index(mid)
            root = TreeNode(mid)
            root.left = buildTree(pre_o[1:i + 1], in_o[:i])
            root.right = buildTree(pre_o[i + 1:], in_o[i + 1:])
            return root
        pre_o = list(map(int, data.split(',')))
        in_o = sorted(pre_o)
        return buildTree(pre_o, in_o)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans