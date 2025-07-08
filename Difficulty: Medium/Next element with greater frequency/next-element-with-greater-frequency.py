from collections import Counter
class Solution:
    def findGreater(self, arr):
        dict=Counter(arr)
        
        n=len(arr)
        ans=[-1]*n
        stack=[]
        
        for i in range(n-1,-1,-1):
            while stack and dict[arr[i]]>=dict[stack[-1]]:
                stack.pop()
            
            if stack:
                ans[i]=stack[-1]
                
            
            stack.append(arr[i])
        return ans
        