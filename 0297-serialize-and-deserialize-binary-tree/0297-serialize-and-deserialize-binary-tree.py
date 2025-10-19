# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ret = []

        def dfs(root):
            if not root:
                ret.append("%")
                return 
            
            ret.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        
        return "#".join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        dat = data.split("#")
        q = deque(dat)

        def dfs(q):
            
            if not q:
                return None

            node = None

            if q[0] == "%":
                q.popleft()
                
            else:
                num = q.popleft()
                node = TreeNode(int(num))
                node.left = dfs(q)
                node.right = dfs(q)

            return node
        
        
        return dfs(q)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))