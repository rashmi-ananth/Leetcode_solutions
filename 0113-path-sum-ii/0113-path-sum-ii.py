# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if root == None:
            return []
        
        return_lst = []
        def dfs(root, lst, total):
            if root.left == None and root.right == None:
                if total  + root.val == targetSum:
                    return_lst.append(lst + [root.val])
                return
            if root.left != None:
                dfs(root.left, lst + [root.val], total + root.val)
            if root.right != None:
                dfs(root.right, lst + [root.val], total + root.val)
            
            

            
            
            
        dfs(root, [], 0)
        return return_lst
        