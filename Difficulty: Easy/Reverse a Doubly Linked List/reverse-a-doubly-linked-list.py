'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        ptr = head
        while ptr:
            a = ptr.prev
            ptr.prev = ptr.next
            ptr.next = a
            if ptr.prev is None:  # means we've reached the new head
                return ptr
            ptr = ptr.prev  # move to next node (originally previous)
