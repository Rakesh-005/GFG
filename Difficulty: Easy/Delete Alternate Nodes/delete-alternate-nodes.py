'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None'''

class Solution:
    def deleteAlt(self, _head):
        # code here
        while _head.next:
            tmp = _head.next
            _head.next = _head.next.next
            _head = tmp