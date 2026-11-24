class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        hours = 0
        while left < right:
            k = (left+right)//2
            hours = sum((pile + k - 1)//k for pile in piles)
            if hours <= h: right = k
            else: left = k + 1
        return left

