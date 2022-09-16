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
            
            difference = abs(root.val - target)
            if  difference < min_val:
                curr_target = root.val
                min_val = difference
                
                
            if root.val > target and root.left:
                dfs(root.left)
                
            if root.val < target and root.right:
                dfs(root.right)
                


            

        
        dfs(root)
        return curr_target
    
    
    
    
    
        