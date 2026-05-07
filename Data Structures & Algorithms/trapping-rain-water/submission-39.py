class Solution:
    def trap(self, heights: List[int]) -> int:
        res, l, r=0, 0, len(heights)-1
        leftmax, rightmax=heights[l], heights[r]
        while l<r:
            if heights[l]<heights[r]:
                l+=1
                leftmax=max(heights[l], leftmax)
                res+=leftmax-heights[l]
            else:
                r-=1
                rightmax=max(heights[r], rightmax)
                res+=rightmax-heights[r]
        return res
                






