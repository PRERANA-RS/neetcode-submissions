"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        old=head
        
        
        
        hashmap={}

        while old:
            
            new = Node(old.val)
            hashmap[old]=new
            old=old.next
        # pass 2 needs its own pointer
        old = head
        while old:
            hashmap[old].random = hashmap[old.random] if old.random else None
            hashmap[old].next = hashmap[old.next] if old.next else None
            old = old.next

        return hashmap[head]  # return the new copy of head