def is_power_of_five(binary_str: str) -> bool:
        if binary_str[0] == '0':
            return False
        num = int(binary_str, 2)
        if num == 0:
            return False
        while num % 5 == 0:
            num //= 5
        return num == 1

class Solution:
    def cuts(self, s):
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # base case: empty string needs 0 parts
    
        for i in range(1, n + 1):
            for j in range(i):
                substring = s[j:i]
                if is_power_of_five(substring):
                    dp[i] = min(dp[i], dp[j] + 1)
    
        return -1 if dp[n] == float('inf') else dp[n]
    
    
