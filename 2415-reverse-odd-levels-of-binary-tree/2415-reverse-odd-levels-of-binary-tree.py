# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root == None or root.left == None:
            return root
        
        
        queue = [root.left, root.right]
        odd = True
        
        while len(queue) > 0:
            
            if odd:
                l, r = 0, len(queue) - 1
                while l < r:
                    queue[l].val, queue[r].val = queue[r].val, queue[l].val
                    l += 1
                    r -= 1
            
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)
            odd = not odd
        return root
                    
                
                
        