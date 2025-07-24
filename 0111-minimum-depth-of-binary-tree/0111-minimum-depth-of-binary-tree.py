# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        q = deque([root])
        i = 1
        while q:
            qlen = len(q)
            for j in range(qlen):
                node = q.popleft()
                if not(node.left) and not(node.right):
                    return i
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            i += 1


            