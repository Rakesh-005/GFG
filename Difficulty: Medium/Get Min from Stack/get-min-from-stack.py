class Solution:

    def __init__(self):
        # code here
        self.s=[]
        self.minEle=None
    # Add an element to the top of Stack
    def push(self, x):
        # code here
        self.minEle = min(x, self.minEle) if self.s else x
        self.s.append(x)

    # Remove the top element from the Stack
    def pop(self):
        # code here
        topEle = self.s.pop() if self.s else -1
        if topEle == self.minEle:
            self.minEle = min(self.s) if self.s else None
        return topEle

    # Returns top element of Stack
    def peek(self):
        # code here
        return self.s[-1] if self.s else -1

    # Finds minimum element of Stack
    def getMin(self):
        # code here
        return self.minEle if self.s else -1



#{ 
 # Driver Code Starts
# Driver Code
if __name__ == '__main__':
    t = int(input())  # Number of test cases

    for _ in range(t):
        q = int(input())  # Number of queries
        stk = Solution()  # Initialize stack
        results = []

        for _ in range(q):
            query = list(map(int, input().split()))

            if query[0] == 1:
                stk.push(query[1])  # Push operation
            elif query[0] == 2:
                stk.pop()  # Pop operation (no return value)
            elif query[0] == 3:
                results.append(str(stk.peek()))  # Peek operation
            elif query[0] == 4:
                results.append(str(stk.getMin()))  # GetMin operation

        print(" ".join(results))  # Print all results in one line
        print("~")

# } Driver Code Ends