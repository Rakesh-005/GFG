#User function Template for python3
class Solution:
    def getLastMoment(self, n, left, right):
        #code here
        res = 0
    
        # Find the time to fall off the plank for all 
        # ants moving towards left
        for i in range(len(left)):
            res = max(res, left[i])
    
        # Find the time to fall off the plank for all 
        # ants moving towards right
        for i in range(len(right)):
            res = max(res, n - right[i])
    
        # Return the maximum time among all ants
        return res


