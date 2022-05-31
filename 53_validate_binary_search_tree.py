# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, minVal, maxValue)-> bool:
            if root is None:
                return True
            
            left = validate(root.left, minVal, root.val)
            right = validate(root.right, root.val, maxValue)
            
            return root.val > minVal and root.val < maxValue and left and right
        
        return validate(root, float("-inf"), float("inf"))
            