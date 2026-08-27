class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = {0: 1}
        current_sum = 0

        for num in nums:
            # 1. Cộng dồn O(1)
            current_sum += num

            # 2. Bước 1: Kiểm tra và cộng count
            if current_sum - k in prefix:
                count += prefix[current_sum - k]

            # 3. Bước 2: Cập nhật tần suất current_sum vào Hash Map
            prefix[current_sum] = prefix.get(current_sum, 0) + 1

        return count