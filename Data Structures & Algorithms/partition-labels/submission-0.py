class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s):
            last[c] = i
        
        size = 0
        end = 0
        res = []

        for i, c in enumerate(s):
            size += 1
            end = max(last[c], end)
            if i == end:
                res.append(size)
                size = 0

        return res