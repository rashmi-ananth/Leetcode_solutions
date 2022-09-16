# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        # TC: O(H) = height of tree ~ O(logN)
        
        curr_target = root.val
        
        def dfs(root):
            nonlocal curr_target
            
            if root == None:
                return
            
            difference = abs(root.val - target)
            if  difference < abs(curr_target - target):
                curr_target = root.val
                min_val = difference
                   
            if root.val > target:
                dfs(root.left) 
            else:
                dfs(root.right)
                

        dfs(root)
        return curr_target
    
    
    
    
    
        