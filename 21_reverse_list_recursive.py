# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        newHead = head
        
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        
        return newHead