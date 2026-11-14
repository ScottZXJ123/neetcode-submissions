class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(start, part):
            if start == len(s):
                res.append(part)
                return 

            for end in range (start + 1, len(s) + 1):
                piece = s[start: end]
                if piece == piece[::-1]:
                    dfs(end, part + [piece])
        
        dfs(0, [])
        return res