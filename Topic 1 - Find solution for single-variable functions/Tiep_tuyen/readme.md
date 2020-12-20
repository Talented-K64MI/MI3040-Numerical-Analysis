# Phương pháp tiếp tuyến - Nhóm 14 - Bùi Tiến Thành
## Input, ouput của chương trình
- Input: Khoảng cách ly nghiệm `L`, `R`; sai số `eps` và biểu thức `f(x)` trong PT f(x) = 0
- Output: Nghiệm bài toán
## Hướng dẫn sử dụng
### Cách 1: Chỉnh sửa trực tiếp vào file `newton_ralphson.py` 
- Bước 1: Uncomment các dòng từ 170 đến 176 và thay các giá trị khoảng cách ly `L`, `R`, sai số `eps` và biểu thức `input_expr` bằng số và biểu thức tương ứng. **CHÚ Ý BIỂU THỨC PHẢI ĐẶT TRONG DẤU NHÁY KÉP ""** 
- Bước 2: Chạy file


### Cách 2: Chạy và làm theo hướng dẫn trong file `main_newton.py`
- **Chú ý:** Comment hết toàn bộ dòng từ 170 đến 176 trong file `newton_ralphson.py` trước khi làm cách này


## Ưu, nhược điểm của phương pháp
- **Ưu điểm:** Tốc độ hội tụ nhanh hơn các phương pháp khác
- **Nhược điểm:**
    - Nhiều ràng buộc về điều kiện hội tụ
    - **Chưa giải được** một số lớp phương trình ví dụ như `sqrt(log(x)) - 1 = 0` do hạn chế của gói tìm Min/Max. _**Đề xuất dùng các phương pháp khác như chia đôi, dây cung, lặp đơn để giải**_

