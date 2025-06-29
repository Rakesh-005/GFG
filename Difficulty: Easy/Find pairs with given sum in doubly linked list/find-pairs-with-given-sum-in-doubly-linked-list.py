from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        res = []
        
        # Set two pointers, first to the beginning of DLL
        # and second to the end of DLL.
        first = head
        second = head
        
        # Move second to the end of the DLL
        while second.next is not None:
            second = second.next
        
        # The loop terminates when two pointers
        # cross each other (second.next == first),
        # or they become the same (first == second)
        while first != second and second.next != first:
            if (first.data + second.data) == target:
              
                # Add pair to the result list
                res.append((first.data, second.data))
                
                # Move first in forward direction
                first = first.next
                
                # Move second in backward direction
                second = second.prev
            elif (first.data + second.data) < target:
                first = first.next
            else:
                second = second.prev
        
        return res
            
