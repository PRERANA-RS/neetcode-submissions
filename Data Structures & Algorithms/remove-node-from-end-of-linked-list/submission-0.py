# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        diff=0
        count=0
        temp1=head
        temp2=head

        while temp1!=None:
            temp1=temp1.next
            count+=1
        diff=count-n
        count=0
        if diff == 0:
            return head.next
        while count<diff -1:
            temp2=temp2.next
            count+=1

        pointer=temp2.next.next
        temp2.next=pointer
        return head
        

