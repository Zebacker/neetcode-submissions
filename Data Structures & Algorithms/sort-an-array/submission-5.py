class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        for i in range(1, len(arr)):
            key = arr[i]  # Lưu giá trị của phần tử hiện tại cần chèn
            j = i - 1
        
        # Di chuyển các phần tử có giá trị lớn hơn 'key'
        # sang phải một vị trí so với vị trí hiện tại của chúng
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
                
            # Chèn 'key' vào vị trí trống thích hợp
            arr[j + 1] = key
        return arr