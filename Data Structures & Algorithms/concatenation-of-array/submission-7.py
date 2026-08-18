class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        b = nums.copy()
        b.extend(nums)
        return b