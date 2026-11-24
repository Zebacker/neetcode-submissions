class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        def rob1(nums):
            n = len(nums)
            if n == 1: return nums[0]
            dp = [0]*(n)
            dp[0] = nums[0]
            dp[1] = max(nums[1], nums[0])
            for z in range(2, n):
                dp[z] = max(dp[z-1], dp[z-2] + nums[z])
            return dp[-1]
        return max(rob1(nums[1:n]), rob1(nums[:n-1]))
