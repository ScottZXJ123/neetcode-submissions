class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = list(range(n+1))
        def find(x):
            while par[x] != x:
                x = par[x]
            return x
        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv:
                return [u, v]
            par[pu] = pv
