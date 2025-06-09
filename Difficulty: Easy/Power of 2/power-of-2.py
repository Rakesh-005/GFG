#User function Template for python3

class Solution:
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self, n):
        # code here
        if n==1:
            return True
        if n%2==0:
            return self.isPowerofTwo( n//2)
        else:
            return False