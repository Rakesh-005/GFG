#User function Template for python3

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        l=set(arr1).intersection(set(arr2)).intersection(set(arr3))
        return sorted(l)