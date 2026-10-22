class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxf = max(count.values())
        maxcount = sum(1 for c in count.values() if c == maxf)
        return max(len(tasks), (maxf-1)*(n+1)+maxcount)
