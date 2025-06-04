
#User function Template for python3

class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
    	# code here 
    	l=[mat[i][j] for j in range(len(mat[0])) for i in range(len(mat))]
        return x in l    	
