class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        vh = []
        for item in nums:
            count[item] = count.get(item, 0) + 1
        for i in count.keys():
            if count[i] > len(nums)//3: vh.append(i)
        return vh
