#User function Template for python3
class Solution:
    def canAttend(self,arr):
        # Your Code Here
        n = len(arr)
        
        # Sort the meetings by their start times
        arr.sort(key=lambda x: x[0])
        
        for i in range(n - 1):
            
            # Compare the current meeting's end time with the 
            # next meeting's start time to check for overlap
            if arr[i][1] > arr[i + 1][0]:
                return False
        return True


