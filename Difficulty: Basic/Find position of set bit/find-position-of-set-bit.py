class Solution:
    def findPosition(self, n):
        a = bin(n)
        if a.count('1') != 1:
            return -1
        return a[2:][::-1].index('1') + 1
