class Solution:
    def findLength(self, c, r):
        stack = []
        for i in range(len(c)):
            if stack and c[i] == c[stack[-1]] and r[i] == r[stack[-1]]:
                stack.pop()  # matching pair, so remove
            else:
                stack.append(i)  # push current index
        return len(stack)
