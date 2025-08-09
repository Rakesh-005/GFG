class Solution:
	def floodFill(self, image, sr, sc, color):
		#Code here
		from collections import deque
        rows, cols = len(image), len(image[0])
        old_color = image[sr][sc]
        if old_color == color:
            return image  # No change needed

        q = deque([(sr, sc)])
        image[sr][sc] = color

        while q:
            r, c = q.popleft()
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == old_color:
                    image[nr][nc] = color
                    q.append((nr, nc))

        return image

