class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        Stack=[-1]
        res=0
        heights.append(0)
        for i in range(len(heights)):
            while Stack and heights[i]<heights[Stack[-1]]:
                h=heights[Stack.pop()]
                w=i-Stack[-1]-1
                res=max(res, h*w)
            Stack.append(i)
        return res

        
            


