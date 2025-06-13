class Solution:
    def countWays(self, s: str) -> int:
        n = len(s)
        s = ' ' + s  # To match 1-based indexing like in C++
        s = list(s)  # Convert to list for character access

        if s[1] == '0':
            return 0

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                dp[i] += dp[i - 2]

        return dp[n]
