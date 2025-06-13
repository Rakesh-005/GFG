'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''        

class Solution:
    def findSpiral(self, root):
        #code here
        q1=[root]
        q2=[]
        ans=[]
        while(q1 or q2):
            if q1:
                for i in q1[::-1]:
                    if i.right:
                        q2.append(i.right)
                    if i.left:
                        q2.append(i.left)
                    ans.append(q1.pop(-1).data)
            else:
                for i in q2[::-1]:
                    if i.left:
                        q1.append(i.left)
                    if i.right:
                        q1.append(i.right)
                    ans.append(q2.pop(-1).data)
        return ans