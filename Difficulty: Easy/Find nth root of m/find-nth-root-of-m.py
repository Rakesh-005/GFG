#User function Template for python3

class Solution:
	def nthRoot(self, n: int, m: int) -> int:
		# Code here
		l=1
		h=m
		while l<=h:
		    mi=(l+h)//2
		    if mi**n==m:
		        return mi
		    elif mi**n>m:
		        h=mi-1
		    else:
		        l=mi+1
	    return -1