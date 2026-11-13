class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = collections.defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                d = abs(x2 - x1) + abs(y2 - y1)
                edges[i].append((j, d))
                edges[j].append((i, d))

        visit = set()
        minheap = [(0, 0)]
        res = 0

        while len(visit) < n:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            res += w1
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, (w2, n2))

        return res
