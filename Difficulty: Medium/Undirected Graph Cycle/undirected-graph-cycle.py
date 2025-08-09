from collections import defaultdict, deque

class Solution:
    def isCycle(self, V, edges):
        gr = defaultdict(list)
        for u, v in edges:
            gr[u].append(v)
            gr[v].append(u)
        
        vis = set()
        q = deque()

        for start in range(V):   # check all components
            if start not in vis:
                q.append((start, -1))  # (node, parent)
                vis.add(start)
                
                while q:
                    node, parent = q.popleft()
                    for nei in gr[node]:
                        if nei not in vis:
                            vis.add(nei)
                            q.append((nei, node))
                        elif nei != parent:
                            return True
        return False
