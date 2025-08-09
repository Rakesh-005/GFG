#User function Template for python3
from collections import defaultdict
class Solution:
    def numProvinces(self, adj, V):
        # code here 
        # n=len(adj)
        # vis=[False]*n
        # cnt=0
        
        # def dfs(i):
        #     for j in range(n):
        #         if vis[j]==False and adj[i][j]==1:
        #             vis[j]=True
        #             dfs(j)
            
        # for i in range(n):
        #     if vis[i]==False:
        #         vis[i]=True
        #         dfs(i)
        #         cnt+=1
        # return cnt
        gr=defaultdict(list)
        for i in range(V):
            for j in range(V):
                if i!=j and adj[i][j]==1:
                    gr[i].append(j)
                    gr[j].append(i)
        n=len(adj)
        vis=[False]*n
        cnt=0
        
        def dfs(i):
            for j in gr[i]:
                if vis[j]==False:
                    vis[j]=True
                    dfs(j)
            
        for i in range(n):
            if vis[i]==False:
                vis[i]=True
                dfs(i)
                cnt+=1
        return cnt