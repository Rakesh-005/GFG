'''
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to return the level order traversal line by line of a tree.
    def levelOrder(self,root):
        
        # code here
        if root is None:
            return []
        ans=[]
        level=[root]
        while level:
            ans.append([node.data for node in level])
            l=[]
            for i in level:
                l.extend([i.left,i.right])
            level=[node for node in l if node]
        return ans