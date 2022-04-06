# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        har, tor = head, head
        
        while har and har.next and har.next.next and tor and tor.next:
            tor = tor.next
            har = har.next.next
            
            if tor == har:
                return True
        
        return False