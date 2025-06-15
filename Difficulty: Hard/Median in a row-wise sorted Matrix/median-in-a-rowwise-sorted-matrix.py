# User function Template for python3

class Solution:
    def median(self, mat):
        arr = []
        for row in mat:
            arr.extend(row)  # flatten the matrix
        arr.sort()
        n = len(arr)
        if (n & 1) == 0:
            return (arr[n // 2] + arr[n // 2 - 1]) // 2  # integer division for median
        else:
            return arr[n // 2]
