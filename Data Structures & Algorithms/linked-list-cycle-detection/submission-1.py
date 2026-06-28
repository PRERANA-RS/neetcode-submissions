# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ls=head
        hs=set()
        if ls== None:
            return False
        while(ls.next!= None):
            if ls.next in hs:
                return True
            
            hs.add(ls.next)
            ls=ls.next
        return False

        