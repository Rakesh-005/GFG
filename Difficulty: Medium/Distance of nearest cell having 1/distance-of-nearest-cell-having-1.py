from collections import deque

class Solution:
    def nearest(self, grid):
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()

        # Step 1: Initialize queue with all 1's and set 0's to inf
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    grid[i][j] = 0  # Distance to itself is 0
                else:
                    grid[i][j] = float('inf')

        # Step 2: BFS from all 1's
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > grid[r][c] + 1:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))

        return grid
