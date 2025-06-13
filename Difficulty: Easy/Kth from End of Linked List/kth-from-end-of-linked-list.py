'''
	A linked list node has the following structure
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to find the data of kth node from the end of a linked list
class Solution:
    def getKthFromLast(self, head, k):
        #code here
        if k<=0:
            return -1
        fast=head
        slow=head
        for i in range(k):
            if fast==None:
                return -1
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        return slow.data