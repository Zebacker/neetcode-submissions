class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        emp = {}
        for item in nums:
            emp[item] = emp.get(item, 0) + 1
        return max(emp, key = emp.get)