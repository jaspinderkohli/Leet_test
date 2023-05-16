# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        lis1 = []
        lis2 = []
        head1 = l2
        while head is not None:
            lis1.append(head.val)
            head = head.next
        
        while head1 is not None:
            lis2.append(head1.val)
            head1 = head1.next
        s_1 = ''
        s_2 = ''
        for i in lis1[::-1]:
            s_1+=str(i)
        for i in lis2[::-1]:
            s_2+=str(i)
        s_3 = int(s_1)+int(s_2)
        s_3 = [int(i) for i in str(s_3)][::-1]
        
        head = ListNode(s_3[0])
        tail = head
        e=1
        while e < len(s_3):
            tail.next = ListNode(s_3[e])
            tail = tail.next
            e+=1
        return head
