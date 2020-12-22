# Phương pháp chia đôi - Nhóm 14 - Bùi Tiến Thành
## Input, ouput của chương trình
- Input: Khoảng cách ly nghiệm `L`, `R`; sai số `eps` và biểu thức `f(x)` trong PT f(x) = 0
- Output: Nghiệm bài toán
## Hướng dẫn sử dụng

### Cách 1: Chạy và làm theo hướng dẫn trong file `main_bisection.py`
Với cách này không cần sửa code, chỉ cần chạy


### Cách 2: Chỉnh sửa trực tiếp vào file `bisection.py` 
- Bước 1: Uncomment 2 dòng 93, 94 và thay các giá trị khoảng cách ly `L`, `R`, sai số `eps` và biểu thức `input_expr` ở dòng 93 bằng biểu thức tương ứng. **CHÚ Ý BIỂU THỨC PHẢI ĐẶT TRONG DẤU NHÁY KÉP ""** 
- Bước 2: Chạy file


## Ưu, nhược điểm của phương pháp
- **Ưu điểm:** Dễ cài đặt, thuật toán đơn giản và giải được hầu hết các lớp phương trình
- **Nhược điểm:**
    - Tốc độ hội tụ chậm
    - Phải có khoảng cách lý nghiệm

## Phụ lục: Giải thích các hàm trong thuật toán
- `bisection_oop`: Gói giải PT bằng PP chia đôi
- `bisection_oop(L, R, eps, f(x))`: Khởi tạo gói với PT `f(x) = 0` trong khoảng cách ly `[L, R]`, sai số `eps`.
- `bisection_oop.__checkInputValidity()`: Kiểm tra ĐK hội tụ
- `bisection_oop.__bisectionMethod()`: Cài giải thuật chia đôi
- `bisection_oop.Solve()`: Hàm giải chính, đưa ra kết quả nghiệm của PT
