class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if abs(target) > sum(nums) or (sum(nums) + target)%2!=0: return 0
        p = (sum(nums)+target)//2
        dp = [0]*(p+1)
        dp[0] = 1
        for i in nums:
            for t in range(p, i-1, -1):
                dp[t] += dp[t-i]
        return dp[p]