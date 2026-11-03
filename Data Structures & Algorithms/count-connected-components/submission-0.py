class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        res = 0

        for start in range(n):
            if start in visit:
                continue
            res += 1
            visit.add(start)
            q = deque([start])
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
        return res