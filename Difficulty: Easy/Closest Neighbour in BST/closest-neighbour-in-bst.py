'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        l = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            l.append(node.data)
            inorder(node.right)
        
        inorder(root)
        
        ans = -1
        for val in l:
            if val <= k:
                ans = val  # Keep updating if val is less than or equal to k
        return ans
