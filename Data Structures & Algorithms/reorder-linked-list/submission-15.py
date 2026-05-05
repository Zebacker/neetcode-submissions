# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        prev, curr=None, slow.next
        slow.next=None

        while curr:
            tem=curr.next
            curr.next=prev
            prev=curr
            curr=tem
        
        head1, head2= head, prev
        while head2:
            f, s=head1.next, head2.next
            head1.next=head2
            if f: head2.next=f
            head1, head2=f, s
            

        
        
