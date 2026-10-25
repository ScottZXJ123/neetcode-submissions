class Solution:
    def numDecodings(self, s: str) -> int:
        prev2, prev1 = 0, 1
        for i in range(1, len(s) + 1):
            count = 0
            if s[i - 1] != "0":
                count += prev1
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                count += prev2
            prev2, prev1 = prev1, count
        return count