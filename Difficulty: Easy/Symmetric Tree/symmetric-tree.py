'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def isSymmetric(self, root):
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (
                t1.data == t2.data and
                isMirror(t1.left, t2.right) and
                isMirror(t1.right, t2.left)
            )

        return isMirror(root.left, root.right) if root else True
