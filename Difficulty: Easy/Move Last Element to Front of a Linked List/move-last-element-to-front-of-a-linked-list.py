from typing import Optional

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""

class Solution:
    def moveToFront(self, head : Optional['Node']) -> Optional['Node']:
        # code here
        l=[]
        ptr=head
        while ptr:
            l.append(ptr.data)
            ptr=ptr.next
        l=[l[-1]]+l[:-1]
        ptr=head
        for i in l:
            ptr.data=i
            ptr=ptr.next
        return head