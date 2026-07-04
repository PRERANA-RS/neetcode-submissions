# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        slow=head
        pointer=None
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        mid = slow
        slow = slow.next
        mid.next = None
        l1=head
        
        prev=None
        curr=slow
        while curr:
            post=curr.next
            curr.next=prev
            prev=curr
            curr=post
        l2=prev
        # after finding slow
      # cut the list in half

        p1=None
        p2=None
        while(l1 and l2):

            p1=l1.next
            l1.next=l2
            p2=l2.next
            
            l2.next = p1
            l1 = p1
            l2 = p2



        