# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        queue1 = [root]
        queue2 = []
        return_lst = []
        temp_lst = []
        
        
        while len(queue1) != 0:
          
            node = queue1.pop(0)
            temp_lst.append(node.val)
            
            if node.left != None:
                queue2.append(node.left)
            if node.right != None:
                queue2.append(node.right)
            
            if len(queue1) == 0:
                queue1 = queue2
                queue2 = []
                return_lst.append(temp_lst)
                temp_lst = []
                
        return return_lst
    
    