class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high # Mặc định tốc độ cao nhất là đáp án an toàn nhất
        
        while low <= high:
            k = (low + high) // 2
            
            # 2. Tính tổng số giờ cần thiết với tốc độ k ngay tại đây
            # Sử dụng công thức (p + k - 1) // k để làm tròn lên mà không cần math.ceil
            total_hours = 0
            for p in piles:
                total_hours += (p + k - 1) // k
                
            # 3. Điều chỉnh biên dựa trên tổng số giờ
            if total_hours <= h:
                res = k         # Tốc độ này ổn, nhưng thử tìm tốc độ nhỏ hơn
                high = k - 1
            else:
                low = k + 1     # Tốc độ quá chậm, phải tăng lên
                
        return res        