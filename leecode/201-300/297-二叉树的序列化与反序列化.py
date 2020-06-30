# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        data = ""
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if node:
                data += str(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                data += "n"
            data += " "
        return data

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        tree = data.split()
        if tree[0] == "n":
            return None
        root = TreeNode(int(tree[0]))
        queue = []
        queue.append(root)
        i = 1
        while queue:
            cur = queue.pop(0)
            if not cur:
                continue
            cur.left = TreeNode(int(tree[i])) if tree[i] != "n" else None
            cur.right = TreeNode(int(tree[i+1])) if tree[i+1] != "n" else None
            i += 2
            queue.append(cur.left)
            queue.append(cur.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
