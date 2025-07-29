class Solution:
    def asciirange(self, s):
        
        
            n=[]
            l={}
            
            for i in range(0,len(s)):
                
                       l[s[i]]=i
            for i in range(0,len(s)):
                        d=0
                
                        if s[i] in l and l[s[i]]!=i:
                            
                            for j in range(i+1, l[s[i]]):
                                d+=ord(s[j])
                            if d!=0:
                             n.append(d)
                            l.pop(s[i])
            
            return(n)