class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num = []
        while val in nums: 
            nums.remove(val)
            num.append("_")
        return len(nums)
            