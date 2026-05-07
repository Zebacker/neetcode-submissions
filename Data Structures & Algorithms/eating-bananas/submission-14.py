class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high=1, max(piles)
        res=high
        while low<=high:
            mid=(low+high)//2
            total_times=0
            for p in piles:
                total_times+=(p+mid-1)//mid
            if total_times <= h: 
                res=mid
                high=mid-1
            else: low=mid+1
        return res 