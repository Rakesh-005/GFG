#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        i=0
        j=0
        num=-1
        while i+j<k:
            if i < len(a) and (j >= len(b) or a[i] <= b[j]):
                num=a[i]
                i+=1
            else:
                num=b[j]
                j+=1
        return num