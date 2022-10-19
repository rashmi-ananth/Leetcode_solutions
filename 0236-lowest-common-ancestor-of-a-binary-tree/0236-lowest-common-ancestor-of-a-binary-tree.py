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
        
        node1 =  self.lowestCommonAncestor(root.left, p, q)
        node2 =  self.lowestCommonAncestor(root.right, p, q)
        
        if node1 != None and node2 != None:
            return root
        if node1 != None:
            return node1
        else:
            return node2
        
        