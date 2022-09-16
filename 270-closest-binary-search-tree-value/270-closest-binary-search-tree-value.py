# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        
        
        min_val = float('inf')
        curr_target = root.val
        
        def dfs(root):
            nonlocal min_val
            nonlocal curr_target
            
            if abs(root.val - target) < min_val:
                curr_target = root.val
                min_val = abs(root.val - target)

            if root.left != None:
                dfs(root.left)
            
            if root.right != None:
                dfs(root.right)
            

        
        dfs(root)
        return curr_target
    
    
    
    
    
        