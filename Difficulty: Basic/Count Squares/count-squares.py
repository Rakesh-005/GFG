#User function Template for python3

class Solution:
    def countSquares(self, n):
        # code here 
        count = 0
        i = 1
        while i * i < n:
            count += 1
            i += 1
        return count