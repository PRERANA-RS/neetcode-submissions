# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp=ListNode(0)
        curr=temp
        if list1==None and list2==None:
            return list1
        if list1==None and list2!=None:
            return list2
        if list2==None and list1!=None:
            return list1

            
        while(list1!=None and list2!=None):
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next  # only list1 moves
            else:
                curr.next = list2
                list2 = list2.next  # only list2 moves
            curr = curr.next  # curr always moves

            
        if list1 !=None:
            curr.next=list1
        if list2!=None:
            curr.next=list2
        return temp.next
