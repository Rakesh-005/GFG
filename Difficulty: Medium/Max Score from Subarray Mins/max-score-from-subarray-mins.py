class Solution:
    def maxSum(self, arr):
        score = 0
        n = len(arr)
        for i in range(1, n):
            score = max(score, arr[i - 1] + arr[i])
        return score
