# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def hasPath(head, root):
            if head is None:
                return True
            elif root is None:
                return False
            else:
                return head.val == root.val and (hasPath(head.next, root.left) or hasPath(head.next,root.right))
        
        if root is None:
            return False
        else:
            return hasPath(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    