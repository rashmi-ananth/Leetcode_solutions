# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None
        
     
        if root.val == p.val or root.val == q.val:
            return root
        

        val1 = self.lowestCommonAncestor(root.left, p, q)

        val2 = self.lowestCommonAncestor(root.right, p, q)
        
        
        if val1 != None and val2 != None:
            return root
        elif val1 != None:
            return val1
        else:
            return val2
        
        
        
        