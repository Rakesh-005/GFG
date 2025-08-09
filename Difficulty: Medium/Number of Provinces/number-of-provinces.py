#User function Template for python3

class Solution:
    def numProvinces(self, adj, V):
        # code here 
        n=len(adj)
        vis=[False]*n
        cnt=0
        
        def dfs(i):
            for j in range(n):
                if vis[j]==False and adj[i][j]==1:
                    vis[j]=True
                    dfs(j)
            
        for i in range(n):
            if vis[i]==False:
                vis[i]=True
                dfs(i)
                cnt+=1
        return cnt