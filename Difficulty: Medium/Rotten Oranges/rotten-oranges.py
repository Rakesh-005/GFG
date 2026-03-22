class Solution:
    def orangesRot(self, mat):
        m, n = len(mat), len(mat[0])
        q = []
        
        fresh = 0
        
        for i in range(m):
            for j in  range(n):
                if mat[i][j] == 2:
                    q.append((i,j, 0))
                elif mat[i][j] == 1:
                    fresh += 1
                    
        mt = 0
        front = 0
        
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        
        while front < len(q):
            r, c, t = q[front]
            front += 1
            
            mt = max(mt, t)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == 1:
                    q.append((nr, nc, t + 1))
                    mat[nr][nc] = 2
                    fresh -= 1 
                    
        return -1 if fresh != 0 else mt