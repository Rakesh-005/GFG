#User function Template for python3

class Solution:
    def makeEven(self, s):
        # code here
        even=0
        for i in s:
            if int(i)%2==0:
                even+=1
        if even==0:
            return s
        for i in range(0,len(s)):
            x=int(s[i])
            if x%2==0:
                if even==1 or  x<int(s[-1]):
                    return s[:i]+s[-1]+s[i+1:len(s)-1]+s[i]
                else:
                    even-=1