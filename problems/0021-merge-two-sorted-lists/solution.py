# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a new linked list to store the merged list
        merged = ListNode()
        curr = merged
        p1 = list1
        p2 = list2
        while p1 and p2:
            # compare the values at the current pointers of the two lists
            if p1.val <= p2.val:
                # add the smaller value to the merged list, and advance the corresponding pointer to the next node
                curr.next = ListNode(p1.val)
                p1 = p1.next
            else:
                curr.next = ListNode(p2.val)
                p2 = p2.next
            curr = curr.next
        # add the remaining elements of the non-exhausted list to the merged list
        curr.next = p1 or p2
        
        # return the head of the merged list
        return merged.next
