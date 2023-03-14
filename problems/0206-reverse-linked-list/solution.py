# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize current prev and next nodes
        current = head
        prev = None
        next_node = None

        # Traverse the list and reverse the pointers
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Set the head of the reversed list to the last node (prev)
        head = prev
        
        return head
