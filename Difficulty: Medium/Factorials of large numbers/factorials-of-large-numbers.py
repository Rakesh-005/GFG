#User function Template for python3

class Solution:
    def factorial(self, n):
        #code here
        l=1
        for i in range(2,n+1):
            l*=i
        return list(str(l))