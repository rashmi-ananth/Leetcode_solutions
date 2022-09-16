# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        # TC: O(N)
        total = 0
        def dfs(root):
            nonlocal total
            
            
            if root.left != None and root.left.left == None and root.left.right == None:
                total += root.left.val
                
            if root.left != None:    
                dfs(root.left)
                
                
            if root.right != None:
                dfs(root.right)
                
            
            
        dfs(root)
        return total
        
        

        