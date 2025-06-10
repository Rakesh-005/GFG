'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        # code here
        ptr=head
        l=[]
        while ptr:
            l.append(ptr.data)
            ptr=ptr.next
        l.sort()
        ptr=head
        for i in l:
            ptr.data=i
            ptr=ptr.next
        return head