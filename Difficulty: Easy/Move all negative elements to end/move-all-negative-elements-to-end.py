#User function Template for python3

class Solution:
    def segregateElements(self, arr):
        # Your code goes here
        l=[i for i in arr if i>=0]+[i for i in arr if i<0]
        for i in range(len(arr)):
            arr[i]=l[i]