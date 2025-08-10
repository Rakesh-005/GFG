#User function Template for python3

from typing import List

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # code here
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            """Marks connected land starting from (i, j) as water using DFS."""
            grid[i][j] = 0  # sink the land cell
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    dfs(x, y)

        # Step 1: Remove all land connected to boundaries
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    dfs(i, j)

        # Step 2: Count remaining land cells (enclaves)
        return sum(sum(row) for row in grid)
