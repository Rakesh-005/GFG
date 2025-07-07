class Solution:
    def nextLargerElement(self, arr):
        # code here
        n = len(arr)
        ans, stack = [-1]*n, []
        
        arr.extend(arr)
        for i, e in enumerate(arr):
            while stack and arr[stack[-1]] < e:
                ans[stack.pop()] = e
            stack.append(i%n)
        return ans