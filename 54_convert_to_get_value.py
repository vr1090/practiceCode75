# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def findDecimal(node:ListNode, current:int)-> int:
            if node is None:
                return current
            else:
                newCurrent = 2 * current + node.val
                return findDecimal(node.next, newCurrent)
        
        return findDecimal(head, 0)
            