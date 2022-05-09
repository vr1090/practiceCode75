class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        elif not root.left and not root.right:
            return root
        
        newLeft = self.invertTree(root.right)
        newRight = self.invertTree(root.left)
        
        root.left = newLeft
        root.right = newRight
        
        return root