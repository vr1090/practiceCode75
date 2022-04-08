# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# the trick ... merge 2 list at a time
# do it again and again

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 :
            return None
        
        
        while len(lists) > 1:
            merged = []
            
            for i in range(0, len(lists), 2):
                first = lists[i]
                second = lists[i+1] if i+1 < len(lists) else 0
                merged.append( self.mergeTwoLists(first, second) )
            
            lists = merged
        
        return lists[0]
    
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        tail = head

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next


        if list1:
            tail.next = list1

        if list2:
            tail.next = list2


        return head.next

