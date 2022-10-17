# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        queue = [root]
        queue2 = []
        odd = False
        
        while len(queue) > 0:
            if odd:
                l, r = 0, len(queue) - 1
                while l < r:
                    queue[l].val, queue[r].val = queue[r].val, queue[l].val
                    l += 1
                    r -= 1
                    
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                    
            odd = not odd
            
            
#             if not odd:
#                 node = queue.pop(0)
#                 if node.left != None:
#                     queue2.append(node.left)
#                 if node.right != None:
#                     queue2.append(node.right)
                    
#             else:
#                 node = queue.pop(0)
#                 node2 = queue.pop()
#                 if node.left != None:
#                     queue2.append(node.left)
#                 if node.right != None:
#                     queue2.append(node.right)
#                 if node2.left != None:
#                     queue2.append(node2.left)
#                 if node2.right != None:
#                     queue2.append(node2.right)
#                 temp = node.val
#                 node.val = node2.val
#                 node2.val = temp
                
                
#             if len(queue) == 0:
#                 queue = queue2
#                 queue2 = []
#                 odd = not odd
                
                
        return root
                
                
                
        