#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        n=len(arr)
        arr.sort()
        duplicate=None
        total_sum=sum(arr)
        for i in range(1,n):
            if arr[i]==arr[i-1]:
                duplicate=arr[i]
                break
        sm=n*(n+1)//2
        missing_no=sm-(total_sum-duplicate)
        return duplicate,missing_no


