#User function Template for python3
class Solution:
    def getSpecialNumber(self, n):
        n -= 1  # adjust for 0-based indexing
        if n < 0:
            return 0
        result = ""
        while n > 0:
            result = str(n % 6) + result
            n //= 6
        return int(result) if result else 0
