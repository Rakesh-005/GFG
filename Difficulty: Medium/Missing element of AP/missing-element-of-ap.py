#User function Template for python3

class Solution:
    def findMissing(self, arr):
        # code here
        d = arr[1] - arr[0]
        n = len(arr)
        for i in range(n-1):
            # AP invariant
            if d != arr[i+1] - arr[i]:
                return arr[i] + d
            
        return arr[-1] + d


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
import math


def main():
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    solution = Solution()

    for i in range(1, t + 1):
        arr = list(map(int, data[i].split()))
        print(solution.findMissing(arr))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends