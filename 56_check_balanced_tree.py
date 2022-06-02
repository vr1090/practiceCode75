# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def depthTree(node:TreeNode):
            if node is None:
                return [True, 0]
            else:
                left = depthTree(node.left)
                right = depthTree(node.right)
                
                
                isBalance = abs(left[1] - right[1]) < 2 and left[0] and right[0]
                currentheight = 1 + max( left[1], right[1])
                
                return [isBalance, currentheight]
        
        result = depthTree(root)
        
        return result[0]
        