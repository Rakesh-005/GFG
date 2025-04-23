#User function Template for python3

class Solution:
	def singleNum(self, arr):
		# Code here
        new=[]
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i,count in freq.items():
            if count==1:
                new.append(i)
        return sorted(new)  


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.singleNum(arr)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends