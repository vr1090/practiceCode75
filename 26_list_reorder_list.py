# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # one in front
        # one in another front
        slow =head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        first = head
        second = slow.next
        slow.next =None
        
        # inverse the second
        prev = None
        
        while second:
            temp = second.next
            second.next =prev
            prev = second
            second = temp
        
        first = head
        second = prev
        
        
        while second:
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2