class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = []
        for s in stones:
            res.append(-s)
        heapq.heapify(res)
        while len(res) > 1:
            y = - heapq.heappop(res)
            x = - heapq.heappop(res)
            if y != x:
                heapq.heappush(res, - (y - x))
        return -res[0] if res else 0