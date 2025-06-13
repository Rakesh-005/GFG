#User function Template for python3
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

class Solution:
    def factorial (self, n):
        # code here
        return fact(n) if n>=0 else -1