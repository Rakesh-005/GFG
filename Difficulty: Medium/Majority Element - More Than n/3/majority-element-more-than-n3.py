class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        l=[]
        n=len(arr)
        for i in set(arr):
            if arr.count(i)>(n/3):
                l.append(i)
        return sorted(l)

