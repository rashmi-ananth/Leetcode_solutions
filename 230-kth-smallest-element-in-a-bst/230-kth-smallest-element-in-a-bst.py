# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        lst = []
        stack = []
        curr = root
        while True:
        
            while curr != None:
                stack.append(curr)
                curr = curr.left

            if len(stack) > 0:
                node = stack.pop()
                lst.append(node.val)
            if len(lst) == k:
                return lst[-1]
            
            
            curr = node.right
                

            
            
        
   
        
#         def dfs(node):
            
#             if node.left != None:
#                 dfs(node.left)

#             lst.append(node.val)
#             if node.right != None:
#                 dfs(node.right)
            
          
#         dfs(root)
#         return lst[k -1]
        
   
        
        
        
        
        