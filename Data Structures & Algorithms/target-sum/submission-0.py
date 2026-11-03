class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        S = sum(nums)
        if abs(target) > S or (S + target) % 2 == 1:
            return 0
        P = (S + target) // 2
        dp = [0] * (P + 1)
        dp[0] = 1
        for x in nums:
            for s in range(P, x - 1, -1):
                dp[s] += dp[s-x]
        return dp[P]