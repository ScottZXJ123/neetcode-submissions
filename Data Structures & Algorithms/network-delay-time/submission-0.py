class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        visit = set()
        minheap = [(0, k)]
        
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 not in visit:
                visit.add(n1)
                t = w1
                for n2, w2 in edges[n1]:
                    heapq.heappush(minheap, (w1 + w2, n2))
        return t if len(visit) == n else -1