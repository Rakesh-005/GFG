#User function Template for python3

class Solution:
    def searchInsertK(self, Arr, k):
        # code here
        if k in Arr:
            return Arr.index(k)
        else:
            if k<=Arr[-1]:
                i=0
                b=len(Arr)
                while Arr[i]<k and i<b:
                    i+=1
                return i
            else:
                return len(Arr)

