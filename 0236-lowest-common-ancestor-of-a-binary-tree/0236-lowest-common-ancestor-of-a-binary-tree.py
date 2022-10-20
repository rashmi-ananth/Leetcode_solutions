# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root == None:
            return None
        
        if root == p or root == q:
            return root
        
        node = self.lowestCommonAncestor(root.left, p, q)
        node2 = self.lowestCommonAncestor(root.right, p, q)
        
        if node != None and node2 != None:
            return root
        if node != None:
            return node
        else:
            return node2