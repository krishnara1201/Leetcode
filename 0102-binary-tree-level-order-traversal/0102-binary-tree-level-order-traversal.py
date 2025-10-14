# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque([root])
        res = []
        
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                level.append(node.val)
            
            if level:
                res.append(level)
        
        return res