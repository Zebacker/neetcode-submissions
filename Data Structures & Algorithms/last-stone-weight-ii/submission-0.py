class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones)
        dp = [False]*((target//2) + 1)
        dp[0] = True
        for i in stones:
            for j in range(target//2, i-1, -1):
                dp[j] = dp[j] or dp[j-i]

        for j in range(target//2, -1, -1):
            if dp[j]: return target - 2*j
        return 0

