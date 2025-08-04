class Solution:
    def maxRectSum(self, mat):
        m, n = len(mat), len(mat[0])
        max_rect_sum = -1000
        for top in range(m):
            col_sums = [0] * n
            for bottom in range(top, m):
                curr_rect_sum = 0
                for col in range(n):
                    col_sums[col] += mat[bottom][col]
                    # Doing Kadane's algorithm
                    curr_rect_sum = max(curr_rect_sum + col_sums[col], col_sums[col])
                    if curr_rect_sum > max_rect_sum:
                        max_rect_sum = curr_rect_sum
        return max_rect_sum
        