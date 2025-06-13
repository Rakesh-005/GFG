'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should print the left view of the binary tree
# Note: You aren't required to print a new line after every test case


class Solution:
    def isSubTree(self, T, S):
        
        def inn(root):
            return inn(root.left) + [root.data] + inn(root.right) if root else []
        
        iT = set(inn(T))
        
        iS = set(inn(S))
        
        return iS <= iT