class Solution:
    def searchMatrix(self, mat, x):
        new_mat = [e for row in mat for e in row]
        return x in new_mat