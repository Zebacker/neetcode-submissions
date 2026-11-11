class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0: return False
        target = s//2
        dp = [False] * (target+1)
        dp[0] = True
        for i in nums:
            for t in range(target, i-1 , -1):
                dp[t] = dp[t] or dp[t-i]
        return dp[target]
        