#User function Template for python3

class Solution:
    def sortedMatrix(self,N,Mat):
        #code here
        space=[Mat[i][j] for i in range(N) for j in range(N)]
        space.sort()
        k=0
        for i in range(N):
            for j in range(N):
                Mat[i][j]=space[k]
                k+=1
        return Mat