class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        sorted_nums = []
        while nums:
            smallest = heapq.heappop(nums)
            sorted_nums.append(smallest)
        return sorted_nums