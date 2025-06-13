#User function Template for python3

class Solution:
    def longestUniqueSubstring(self, s):

        r=set()

        ind=0

        m=0

        for i in range(len(s)):

            if s[i] not in r:

                r.add(s[i])

                m=max(m,i-ind+1)

            else:

                while s[i] in r:

                    r.remove(s[ind])

                    ind+=1

                r.add(s[i])

        return(m)