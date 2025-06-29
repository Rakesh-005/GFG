#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


# your task is to complete this function
# function should return true/false or 1/0
class Solution:
    def isCircular(self, head):
        # Code here
        f=head
        s=head
        while f and f.next:
            f=f.next.next
            s=s.next
            if f==s:
                return True
        return False