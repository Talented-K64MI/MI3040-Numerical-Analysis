# Phương pháp tiếp tuyến - Nhóm 14 - Bùi Tiến Thành
## Input, ouput của chương trình
- Input: Khoảng cách ly nghiệm `L`, `R`; sai số `eps` và biểu thức `f(x)` trong PT f(x) = 0
- Output: Nghiệm bài toán
## Hướng dẫn sử dụng

### Cách 1: Chạy và làm theo hướng dẫn trong file `main_newton.py`
Với cách này không cần sửa code, chỉ cần chạy


### Cách 2: Chỉnh sửa trực tiếp vào file `newton_ralphson.py` 
- Bước 1: Uncomment các dòng từ 170 đến 176 và thay các giá trị khoảng cách ly `L`, `R`, sai số `eps` và biểu thức `input_expr` bằng số và biểu thức tương ứng. **CHÚ Ý BIỂU THỨC PHẢI ĐẶT TRONG DẤU NHÁY KÉP ""** 
- Bước 2: Chạy file



## Ưu, nhược điểm của phương pháp
- **Ưu điểm:*newton_oop* Tốc độ hội tụ nhanh hơn các phương pháp khác
- **Nhược điểm:**
    - Nhiều ràng buộc về điều kiện hội tụ
    - **Chưa giải được** một số lớp phương trình ví dụ như `sqrt(log(x)) - 1 = 0` do hạn chế của gói tìm Min/Max và trong gói Min/Max còn bỏ qua các điểm làm đạo hàm không xác định _**Đề xuất dùng các phương pháp khác như chia đôi, dây cung, lặp đơn để giải**_


## Phụ lục: Giải thích các hàm trong thuật toán
- `newton_oop`: Gói giải PT bằng PP chia đôi
- `newton_oop(L, R, eps, f(x))`: Khởi tạo gói với PT `f(x) = 0` trong khoảng cách ly `[L, R]`, sai số `eps`.
- `newton_oop.__checkInputValidity()`: Kiểm tra ĐK hội tụ
- `newton_oop.__findMaxMin(f)`: Tìm max, min của hàm f và dấu của chúng thông qua đạo hàm. Hàm này trả về bộ 4 phần tử, từ trái sang phải gồm:
    - Min của f
    - Max của f
    - Dấu của min f
    - Dấu của max f
- `newton_oop.__newtonMethod()`: Cài giải thuật tiếp tuyến
- `newton_oop.Solve()`: Hàm giải chính, đưa ra kết quả nghiệm của PT
