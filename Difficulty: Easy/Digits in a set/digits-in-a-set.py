#User function Template for python3

class Solution:
    # Function to count the numbers satisfying the given condition.
    def countNumbers(self, n):
        # code here
        c=0
        for i in range(1,n+1):
            ok=True
            for j in str(i):
                if j not in '1,2,3,4,5':
                    ok=False
            if ok:
                c+=1
        return c