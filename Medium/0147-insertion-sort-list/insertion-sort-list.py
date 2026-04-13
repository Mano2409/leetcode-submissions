# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

        if not head:
            return head
        
        dummy = ListNode(0)
        curr = head
        
        while curr:
            # At each step, find where to insert curr
            prev = dummy
            
            # Find the position
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            # Insert curr between prev and prev.next
            next_node = curr.next
            curr.next = prev.next
            prev.next = curr
            
            # Move to next node in original list
            curr = next_node
            
        return dummy.next

        