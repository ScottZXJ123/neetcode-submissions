class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                j = i + len(w)
                if j <= len(s) and s[i: j] == w and dp[j]:
                    dp[i] = True
                    break
        return dp[0]
