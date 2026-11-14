class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 + len2 != len(s3):
            return False
        
        spots = {(0, 0)}
        for ch in s3:
            newspots = set()
            for i, j in spots:
                if i < len1 and s1[i] == ch:
                    newspots.add((i + 1, j))
                if j < len2 and s2[j] == ch:
                    newspots.add((i, j + 1))
            spots = newspots

        return (len(s1), len(s2)) in spots