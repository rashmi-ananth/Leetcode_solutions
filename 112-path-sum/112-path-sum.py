# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        def dfs(root, total):
            
            if root.left == None and root.right == None:
                if total + root.val == targetSum:
                    return True
                else:
                    return False
            left, right = False, False
            if root.left != None:
                left = dfs(root.left, total + root.val)
            if root.right != None:
                right = dfs(root.right, total + root.val)
            
            return max(left, right)
            
            
            
        return dfs(root, 0)
        